from stats import count_words
from stats import count_characters_in_text

def get_book_text(path) -> str:
    """
    Reads the content of a book file and returns it as a string.

    Args:
        path (str): The path to the book file.

    Returns:
        str: The content of the book file.
    """
    with open(path) as file:
        text = file.read()
    return text

def main():
    """
    Main function to execute the script.
    """
    book_text = get_book_text('./books/frankenstein.txt')

    num_words = count_words(book_text)
    characters_in_text = count_characters_in_text(book_text)
    print(f"{num_words} words found in the document.")
    print(characters_in_text)

main()