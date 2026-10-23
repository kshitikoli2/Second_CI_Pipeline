def is_sorted(numbers):
    """Return True when numbers are in non-decreasing order."""
    return all(numbers[index] <= numbers[index + 1] for index in range(len(numbers) - 1))
