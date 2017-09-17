"""Quick and dirty markdown to rst converter.

This file is here just because I used it when setting up sphinx and
someone else might find it useful.
"""

import glob
import re
from functools import partial


def header(m):
    n = len(m.group(1))
    s = m.group(2)
    return s + '\n' + '=~'[n-1]*len(s)


def fix(s):
    s = re.sub(r'^(#+) (.*)$', header, s, flags=re.MULTILINE)
    s = re.sub(r'^\[math:.+\]: images/math/[0-9a-f]{32}.gif$',
               '', s, flags=re.MULTILINE).rstrip()
    s += '\n'
    s = re.sub(r'`(.+?)`', r'``\1``', s)
    s = re.sub(r'!\[math:(.+?)\]\[\]', r'`\1`', s)       # must be after processing md `code`
    s = re.sub(r'!\[.+?\]\((.+?)\)', r'.. image:: \1', s)
    s = re.sub(r'\[(.+?)\]\((.+?)\)', r'`\1 <\2>`_', s)
    return s


def main():
    for md in glob.glob('*.md'):
        print(md)
        with open(md, 'r') as f:
            before = f.read()
        after = fix(before)
        with open(md[:-2] + 'rst', 'w') as f:
            f.write(after)


if __name__ == '__main__':
    main()
