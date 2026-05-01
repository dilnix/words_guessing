"""
The words quessing helper.
Helps to find possible matching words based on the given conditions.
"""


def collect_conditions():
    """
    Collects the conditions from the user.
    """
    conditions = {}
    conditions["word_length"] = int(input("Enter the length of the word: "))
    conditions["excluded_letters"] = set(input("Enter the excluded letters: ").lower())
    conditions["required_letters"] = set(input("Enter the required letters: ").lower())

    true_positions = {
        i: letter
        for i in range(conditions["word_length"])
        if (letter := input(f"Enter the known letter for position {i + 1}: ").lower())
        != ""
    }

    false_positions = {}
    for letter in conditions["required_letters"]:
        raw = input(
            f"Enter positions where '{letter}' is NOT (comma-separated, 1-based), or blank: "
        ).strip()
        if raw:
            false_positions[letter] = {
                int(p) - 1 for p in raw.split(",") if p.strip().isdigit()
            }

    return conditions, true_positions, false_positions


def check_word(
    word,
    word_length,
    required_letters,
    excluded_letters,
    true_positions,
    false_positions,
) -> bool:
    """
    Checks if the given word matches the conditions.
    """

    if len(word) != word_length:
        return False

    for i, letter in true_positions.items():
        if word[i] != letter:
            return False

    if not required_letters.issubset(set(word)):
        return False

    if any(letter in excluded_letters for letter in word):
        return False

    for letter, disallowed_positions in false_positions.items():
        if any(word[i] == letter for i in disallowed_positions):
            return False

    return True


def main() -> None:
    """
    The main function.
    """
    conditions, true_positions, false_positions = collect_conditions()
    word_length = conditions["word_length"]
    required_letters = conditions["required_letters"]
    excluded_letters = conditions["excluded_letters"]

    with open("./dictionary.txt") as f:
        words: list[str] = f.read().splitlines()

    for word in words:
        if check_word(
            word,
            word_length,
            required_letters,
            excluded_letters,
            true_positions,
            false_positions,
        ):
            print(f"Found a matching word: {word.upper()}")


if __name__ == "__main__":
    main()
