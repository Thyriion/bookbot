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

    print(book_text)

main()