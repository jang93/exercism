import re


def abbreviate(words):
    matches = re.findall(r'[A-Z\']+', words.upper())
    return ''.join([match[0] for match in matches])

