{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE QuasiQuotes #-}
{-# LANGUAGE FlexibleContexts #-}

module Main where

--
-- Renumbers the turtle.md section headings and generates the TOC.
--

import           Control.Monad         (unless, when)
import           Control.Monad.State   (State, get, put, execState)
import qualified Data.Text          as T
import qualified Data.Text.IO       as T
import           System.Directory      (doesFileExist)
import           System.Environment    (getArgs, getProgName)
import           Text.Regex.PCRE.Heavy (Regex, re, scan)

-- Types

type Heading = (T.Text, T.Text, T.Text, T.Text)

data ParseState = Intro | TOC | Body deriving Show

data HState = HState
    { lastLen    :: Int
    , previous   :: [Int]
    , parseState :: ParseState
    , headings   :: [Heading]
    , intro      :: [T.Text]
    , body       :: [T.Text]
    } deriving Show

newtype Result = Result ([Heading], [T.Text], [T.Text]) deriving Show

-- Utility

headMay :: [a] -> Maybe a
headMay xs | null xs   = Nothing
           | otherwise = Just $ head xs

endsWith :: T.Text -> T.Text -> Bool
endsWith s suffix = T.takeEnd (T.length suffix) s == suffix

-- Parsing

headingRe :: Regex
headingRe = [re|^(#+) <a name="([a-z][a-z0-9_]*)"></a>(\d+(?:\.\d+)*)(?:&nbsp;){3}(.*)|]

getHeading :: T.Text -> Maybe Heading
getHeading line =
    case m of
        Just (_, h@[_, _, _, _]) -> Just (hFromList h)
        _ -> Nothing
    where m = headMay $ scan headingRe line
          hFromList :: [T.Text] -> Heading
          hFromList [a,b,c,d] = (a,b,c,d)
          hFromList _ = error "list length mismatch"

-- Unparsing

numsToString :: [Int] -> T.Text
numsToString = T.intercalate "." . map (T.pack . show)

toAnchor :: T.Text -> T.Text
toAnchor s = "<a name=\"" <> s <> "\"></a>"

-- Converts a parsed heading into a flat markdown string.
headingToString :: Heading -> T.Text
headingToString (level, anchor, section, title)
    = level <> " " <> toAnchor anchor <> section <> ws <> title
    where ws = "&nbsp;&nbsp;&nbsp;"

-- Builds a line suitable for a TOC entry.
headingToLink :: Heading -> T.Text
headingToLink (level, anchor, section, title)
    = indent <> "* " <> section <> ws
             <> "[" <> title <> "]"
             <> "(#" <> anchor <> ")"
    where
        indent = T.pack $ replicate (T.length level - 2) '\t'
        ws = "&nbsp;&nbsp;&nbsp;"

-- Renumbering logic

renumberLine :: Heading -> State HState ()
renumberLine (level, anchor, _, title) =
    let
        hlen = T.length level
        setLevel ns = do
            let h = (level, anchor, numsToString ns, title)
            state <- get
            put state { lastLen  = hlen
                      , previous = ns
                      , headings = h : headings state
                      , body     = headingToString h : body state }
    in do
        state <- get
        let p = previous state
        if hlen > lastLen state
        then if hlen /= lastLen state + 1
             then error "found heading increase of more than one level"
             else setLevel (p ++ [1])
        else do
            let p' = if hlen < lastLen state
                     then take (hlen-1) p
                     else p
            setLevel (init p' ++ [last p' + 1])

tocBegin :: T.Text
tocBegin = "## Table of Contents"

processLine :: T.Text -> State HState ()
processLine line = do
    state <- get
    case parseState state of
        Intro -> do
            put state { intro = line : intro state }
            when (line == tocBegin) $
                put state { parseState = TOC }
        TOC ->
            case getHeading line of
                Nothing -> pure ()
                Just heading -> do
                    put state { parseState = Body }
                    renumberLine heading
        Body ->
            case getHeading line of
                Nothing -> put state { body = line : body state }
                Just heading -> renumberLine heading

renumber :: [T.Text] -> Result
renumber xs = Result ( reverse $ headings state
                     , reverse $ intro state
                     , reverse $ body state )
    where initLevel = HState { lastLen = 2
                             , previous = [0]
                             , parseState = Intro
                             , headings = []
                             , intro = []
                             , body = [] }
          state = execState (mapM processLine xs) initLevel

-- Validation and file path stuff

check :: Bool -> T.Text -> IO ()
check cond msg = unless cond (error $ T.unpack msg)

getPath :: IO FilePath
getPath = do
    args <- getArgs
    progName <- getProgName
    check (length args == 1) $
          "Usage: " <> T.pack progName <> " <file>"

    let path = head args

    exists <- doesFileExist path
    check exists
          ("Error: path does not exist: " <> T.pack path)

    check (T.pack path `endsWith` ".md")
          ("Error: not a markdown file (with '.md' extension): " <> T.pack path)

    pure path

buildToc :: [Heading] -> T.Text
buildToc = T.unlines . map headingToLink

mergeResult :: Result -> T.Text
mergeResult (Result (hs, i, b)) =
    T.unlines $ i ++ [tocBegin, "", buildToc hs] ++ b

main :: IO ()
main = do
    path <- getPath
    contents <- T.readFile path
    let result = renumber $ T.lines contents
    T.writeFile path $ mergeResult result
