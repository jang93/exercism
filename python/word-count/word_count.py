import re
from collections import Counter

def count_words(sentence):
    pattern = re.compile(r'''
    (\d+ |                           # numbered word
    [a-z]+(?:'[a-z]+)?)              # apostrophed word (match before lettered word as lettered word is a subset)
    ''', re.VERBOSE | re.I)
    matches = pattern.findall(sentence)
    return Counter([match.lower() for match in matches])