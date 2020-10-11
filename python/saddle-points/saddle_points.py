def saddle_points(matrix):
    if len(matrix) == 0:
        return []
    try:
        biggest_in_row = set()
        for i in range(len(matrix)):
            biggest = max(matrix[i])
            for j in range(len(matrix[i])):
                if matrix[i][j] == biggest:
                    biggest_in_row.add((i,j))
        smallest_in_column = set()
        for j in range(len(matrix[0])):
            smallest = min([matrix[i][j] for i in range(len(matrix))])
            for i in range(len(matrix)):
                if matrix[i][j] == smallest:
                    smallest_in_column.add((i,j))
    except IndexError:
        raise ValueError('Matrix is irregular')

    # Another method is to transpose the matrix using zip(*matrix)

    return [{"row": points[0]+1, "column": points[1]+1}for points in biggest_in_row.intersection(smallest_in_column)]

