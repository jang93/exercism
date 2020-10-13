def triplets_with_sum(number):
    triplets = []
    for a in range(1, number // 3):
        for b in range(a + 1, number // 2):
            c = number - a - b
            if c**2 == a**2 + b**2:
                triplets.append([a, b, c])
    return triplets


def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    pass
