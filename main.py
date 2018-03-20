#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import StringIO

import csv


def main():
    rows = [
        ['🍣'],
        ['髙﨑 將'],
        ['あああ', 'いいい', 'ううう'],
        ['Ⅰ・Ⅱ・Ⅲ', '①②③'],
        [1, 2, 3],
        ['1', '2', '3'],
    ]

    f = StringIO()
    writer = csv.writer(f, dialect='excel-tab')
    writer.writerows(rows)
    f.seek(0)

    with open('./unicode.csv', 'w', newline='', encoding='utf-16') as out:
        out.write(f.read())


if __name__ == '__main__':
    main()
