
import re

def is_valid(isbn):
    pattern = re.compile(r'''
    ^(\d)       # First Number
    -?          # Optional dash
    (\d{3})       # Next 3 Numbers
    -?          # Optional Dash
    (\d{5})       # Next 5 Numbers
    -?          # Optional Dash
    ([0-9X])$     # Last 3 Numbers
    ''', re.VERBOSE)
    match = pattern.search(isbn)
    if match is None:
        return False

    isbn_list = list(''.join([match.group(1), match.group(2), match.group(3)]))
    if match.group(4).lower() == 'x':
        isbn_list.append('10')
    else:
        isbn_list.append(match.group(4))

    return sum([a*int(b) for a, b in zip(range(10, 0, -1), isbn_list)]) % 11 == 0


