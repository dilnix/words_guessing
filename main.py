"""
The words quessing helper.
Helps to find possible matching words based on the given conditions.
"""


def position_input(i) -> str:
    """
    Collects the known letter for the given position.
    """
    letter: str = input(f"Enter the known letter for position {i+1}: ").lower()
    return letter


def collect_conditions():
    """
    Collects the conditions from the user.
    """
    conditions = {}
    conditions['word_length'] = int(input("Enter the length of the word: "))
    conditions['excluded_letters'] = set(input("Enter the excluded letters: ").lower())
    conditions['required_letters'] = set(input("Enter the required letters: ").lower())

    positions = {}
    for i in range(conditions['word_length']):
        positions[i] = position_input(i)
    return conditions, positions


def check_word(word, conditions, positions) -> bool:
    """
    Checks if the given word matches the conditions.
    """

    if len(word) != conditions['word_length']:
        return False

    # Check the known letters
    for i, letter in positions.items():
        if letter != '' and word[i] != letter:
            return False

    if not conditions['required_letters'].issubset(set(word)):
        return False

    if any(letter in conditions['excluded_letters'] for letter in word):
        return False

    return True


def main() -> None:
    """
    The main function.
    """
    conditions, positions = collect_conditions()

    # Load a dictionary of words (replace with your dictionary file)
    words = []
    with open('./dictionary.txt') as f:
        words: list[str] = f.read().splitlines()

    for word in words:
        if check_word(word, conditions, positions):
            print(f"Found a matching word: {word.upper()}")


if __name__ == "__main__":
    main()
