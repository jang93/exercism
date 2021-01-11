SCORING = {
    'AEIOULNRST': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
}


def score(word):
    score = 0
    for key, value in SCORING.items():
        for letter in word.upper():
            if letter in key:
                score += value
    return score

