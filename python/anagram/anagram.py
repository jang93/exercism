import collections


def find_anagrams(word, candidates):
    word_counter = collections.Counter(word.lower())
    return [candidate for candidate in candidates if word_counter == collections.Counter(candidate.lower()) and candidate.lower() != word.lower()]
