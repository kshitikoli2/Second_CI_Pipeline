def move_zeros(numbers):
    """Return a new list with all zero values moved to the end."""
    non_zeros = [number for number in numbers if number != 0]
    zeros = [number for number in numbers if number == 0]
    return non_zeros + zeros
