#!/usr/bin/env python

"""
Renumbers the turtle.md section headings and generates the table of contents.
"""

import os
import sys
import re


# Constants

TOC_BEGIN = '## Table of Contents\n'

HEADING_RE = '^(#+) <a name="([a-z]+)"><\/a>(\d+(?:\.\d+)*)(?:&nbsp;){3}(.*)'


# Global utility functions

def check(cond, msg):
    if not cond:
        sys.stderr.write(msg)
        sys.exit(-1)

def split_unnumbered(heading):
    return tuple(map(lambda x: x.strip(),
                     heading.split(' ', 1)))

def split_heading(heading):
    m = re.match(HEADING_RE, heading)
    if not m:
        return (False, split_unnumbered(heading))
    return (True, m.groups())

def unsplit_heading((numbered, tpl)):
    if not numbered:
        return ' '.join(tpl) + '\n'
    (level, anchor, number, title) = tpl
    fmt = '{0} <a name="{1}"></a>{2}{3}{4}\n'
    return fmt.format(level, anchor, number, '&nbsp;'*3, title)

def unsplit_link((_, anchor, number, title)):
    indent = len(number.split('.'))-1
    assert(indent >= 0)
    fmt = '{0}* {1}{2}[{3}](#{4})\n'
    return fmt.format('\t'*indent,
                      number,
                      '&nbsp;'*3,
                      title,
                      anchor)

def filter_numbered(headings):
    filtered = [h for (numbered, h) in headings if numbered]
    return filtered

def get_lengths(headings):
    filtered = filter_numbered(headings)
    lengths = [len(h[0]) for h in filtered]
    return lengths

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

    prev = lengths[0]
    result = [[1]]
    for length in lengths[1:]:
        if length > prev:
            check(length == prev + 1,
                  "found heading increase of more than one level")
            r = result[-1][:]
            result.append(r + [1])
        else:
            r = result[-1][:]
            if length < prev:
                r = result[-1][:length-1]
            result.append(r[:-1] + [r[-1]+1])
        prev = length
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
        with open(self.path, 'w') as f:
            for line in self.lines:
                if line.startswith('#'):
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
        return [i for i, line in enumerate(self.lines)
                if line.startswith('#')]

# Main

def main():
    Renumber(get_path()).process()


if __name__ == '__main__': main()
