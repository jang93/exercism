def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Both strands are of unequal length.")

    return sum([letter_a != letter_b for letter_a, letter_b in zip(strand_a, strand_b)])
