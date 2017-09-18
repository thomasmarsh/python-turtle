#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Renumbers the turtle.md section headings and generates the table of contents.
"""

import os
import sys
import re


# Constants

TOC_BEGIN = '## Table of Contents\n'


# Heading format

"""
A parsed heading is of the form `(numbered, tpl)` where `numbered` is a boolean,
indicating whether this is a numbered section. The `tpl` component has a
different structure depending on `numbered`. If `numbered` is True, it has the
following format:

    (level,     # header level string     (e.g., '##' for H2)
     anchor,    # anchor 'name' attribute (e.g., 'draw')
     number,    # section number          (e.g., '3.4.1')
     title)     # section title           (e.g., 'Moiré Patterns')

If not numbered, then it is simply a two-tuple:

    (level,     # heading level string    (e.g., '##' for H2)
     title)     # section title           (e.g, 'Introduction')
"""

# Regex to match a numbered heading
HEADING_RE = '^(#+) <a name="([a-z]+)"><\/a>(\d+(?:\.\d+)*)(?:&nbsp;){3}(.*)'

def split_heading(heading):
    m = re.match(HEADING_RE, heading)
    if not m:
        return (False, split_unnumbered(heading))
    return (True, m.groups())

def split_unnumbered(heading):
    return tuple(map(lambda x: x.strip(),
                     heading.split(' ', 1)))

def unsplit_heading((numbered, tpl)):
    """
    Converts a parsed heading into a flat markdown string.
    """
    if not numbered:
        return ' '.join(tpl) + '\n'
    (level, anchor, number, title) = tpl
    fmt = '{0} <a name="{1}"></a>{2}{3}{4}\n'
    return fmt.format(level, anchor, number, '&nbsp;'*3, title)

def unsplit_link((_, anchor, number, title)):
    """
    Builds a line suitable for a TOC entry.
    """
    indent = len(number.split('.'))-1
    assert(indent >= 0)
    fmt = '{0}* {1}{2}[{3}](#{4})\n'
    return fmt.format('\t'*indent,
                      number,
                      '&nbsp;'*3,
                      title,
                      anchor)

# Global utility functions

def check(cond, msg):
    if not cond:
        sys.stderr.write(msg)
        sys.exit(-1)

def indices_matching(cond, xs):
    return [i for i, line in enumerate(xs)
            if cond(line)]

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield tuple(l[i:i + n])

def filter_numbered(headings):
    return [h for (numbered, h) in headings if numbered]

def get_lengths(headings):
    filtered = filter_numbered(headings)
    return [len(h[0]) for h in filtered]

def renumber(headings):
    lengths = get_lengths(headings)
    numbers = enumerate_headings(lengths)
    result = []
    i = 0
    for (numbered, tpl) in headings:
        if not numbered:
            result.append((numbered, tpl))
        else:
            (level, anchor, _, title) = tpl
            assert(i < len(numbers))
            num_str = '.'.join([str(x) for x in numbers[i]])
            result.append((numbered, (level, anchor, num_str, title)))
            i += 1
    return result

def enumerate_headings(lengths):
    check(len(lengths) > 0, "no numbered headings found")
    check(min(lengths) == 2,
          "numbered headings must be H2 at largest (got %d)" % min(lengths))
    check(lengths[0] == 2,
          "first heading must be level H2 (got H%d)" % lengths[0])

    last_len = lengths[0]
    result = [[1]]
    for length in lengths[1:]:
        # Previous result. Note: do not mutate
        prev = result[-1]

        if length > last_len:
            check(length == last_len + 1,
                  "found heading increase of more than one level")
            result.append(prev + [1])
        else:
            if length < last_len:
                prev = prev[:length-1]
            result.append(prev[:-1] + [prev[-1]+1])
        last_len = length
    return result

def get_path():
    check(len(sys.argv) == 2,
          'Usage: toc.py <file>')

    [_, path] = sys.argv

    check(os.path.exists(path), 
          'Error: path does not exists: ' + path)

    check(path.endswith('.md'),
          'Error: not a markdown file (with \'.md\' extension): ' + path)

    return path


# The main processing class

class Renumber:
    def __init__(self, path):
        self.path = path
        with open(path, 'r') as f:
            self.lines = f.readlines()
        self.headings = self.find_headings()

    def write_toc(self, f, headings):
        f.write(TOC_BEGIN)
        f.write('\n')
        for (numbered, h) in headings:
            if numbered:
                f.write(unsplit_link(h))
        f.write('\n')

    def process(self):
        renumbered = renumber(self.headings)
        i = 0
        skip = False
        code_block = False
        with open(self.path, 'w') as f:
            for line in self.lines:

                if line.startswith == '```':
                    code_block = not code_block

                if not code_block and line.startswith('#'):
                    if line == TOC_BEGIN:
                        skip = True
                        self.write_toc(f, renumbered)
                    else:
                        skip = False
                        assert(i < len(renumbered))
                        f.write(unsplit_heading(renumbered[i]))
                    i += 1
                else:
                    if not skip:
                        f.write(line)

    def find_headings(self):
        return [split_heading(self.lines[i])
                for i in self.find_heading_indices()]

    def find_heading_indices(self):
        code_blocks = indices_matching(lambda x: x.startswith('```'),
                                       self.lines)
        check(len(code_blocks) % 2 == 0,
              'Error: unbalanced code block delimiters detected in file')

        pairs = chunks(code_blocks, 2)

        # A line is a header if it starts with '#' and is not within
        # a code block.
        def is_header((n, line)):
            return (not any(a <= n <= b for (a, b) in pairs)
                    and line.startswith('#'))

        return indices_matching(is_header, enumerate(self.lines))

# Main

def main():
    Renumber(get_path()).process()


if __name__ == '__main__': main()
