import re
import collections

def count_words(sentence):
    pattern = re.compile(r'''
    (\d+ |                     # numbered word
    [a-z]+'?[a-z]+ |           # apostrophed word (match before lettered word as lettered word is a subset)
    [a-z]+)                    # lettered word
    ''', re.VERBOSE | re.I)
    matches = pattern.findall(sentence)
    return dict(collections.Counter([match.lower() for match in matches]))