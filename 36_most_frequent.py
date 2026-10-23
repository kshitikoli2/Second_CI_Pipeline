def most_frequent(numbers):
    """Return the most frequent item; ties go to the item seen first. Empty input returns None."""
    if not numbers:
        return None
    counts = {}
    for item in numbers:
        counts[item] = counts.get(item, 0) + 1
    highest_count = max(counts.values())
    for item in numbers:
        if counts[item] == highest_count:
            return item
