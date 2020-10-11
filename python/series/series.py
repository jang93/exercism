def slices(series, length):
    if length > len(series):
        raise ValueError("Length cannot be more than length of series")
    elif length <= 0:
        raise ValueError("Length cannot be 0")
    return [series[i:i+length] for i in range(len(series)-length+1)]
