def is_isogram(string):
    string = list(string.replace("-", "").replace(" ", "").lower())
    return len(string) == len(set(string))