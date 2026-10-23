def rotate_string(text, k):
    """Rotate text right by k positions. Negative k rotates left."""
    if not text:
        return text
    k %= len(text)
    if k == 0:
        return text
    return text[-k:] + text[:-k]
