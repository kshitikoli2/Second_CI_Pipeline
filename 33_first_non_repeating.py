def first_non_repeating(text):
    """Return the first character occurring once, or None if none exists."""
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    for char in text:
        if counts[char] == 1:
            return char
    return None
