def missing_number(nums):
    """Find the missing value from the range 0..n, where nums has n distinct values."""
    result = len(nums)
    for index, value in enumerate(nums):
        result ^= index ^ value
    return result
