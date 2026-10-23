def transpose_matrix(matrix):
    """Return the transpose of a rectangular matrix."""
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]
