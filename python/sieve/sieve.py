def primes(limit):
    unmarked = list(range(2,limit+1))
    ind = 0
    while ind + 1 <= len(unmarked):
        for i in range(unmarked[ind]*2, limit+1, unmarked[ind]):
            if i in unmarked: unmarked.remove(i)
        ind += 1
    return unmarked
