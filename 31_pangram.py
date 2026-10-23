def is_pangram(sentence):
    """Return True if sentence contains every English letter a-z."""
    letters = {char.lower() for char in sentence if char.isalpha() and char.isascii()}
    return all(chr(code) in letters for code in range(ord("a"), ord("z") + 1))
