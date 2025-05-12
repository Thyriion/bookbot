def count_words(text: str) -> int:
    """
    Counts the number of words in a given text.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def count_characters_in_text(text: str) -> dict[str, int]:
    """
    Counts the number of characters in a given text.

    Args:
        text (str): The text to count characters in.

    Returns:
        dict[str, int]: A dictionary with character counts.
    """
    char_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count