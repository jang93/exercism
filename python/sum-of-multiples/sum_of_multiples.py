def sum_of_multiples(limit, multiples):
    return sum([i if any([multiple and i % multiple == 0 for multiple in multiples]) else 0 for i in range(limit)])
