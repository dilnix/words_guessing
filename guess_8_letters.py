def check_word(word):
    excluded_letters = {'W', 'R', 'Y', 'I', 'P', 'A', 'S', 'D', 'G', 'H', 'L', 'X', 'C', 'V'}
    required_letters = {'T', 'U', 'M'}

    if len(word) != 8:
        return False

    # Explicitly check each position
    if word[5] != 'e':  # Check for 'e' at index 5 (6th position)
        return False

    if not required_letters.issubset(set(word.upper())):
        return False

    if any(letter in excluded_letters for letter in word.upper()):
        return False

    return True

# Load a dictionary of words (replace with your dictionary file)
words = []
with open('/home/dilnix/Projects/python/words_guessing/dictionary.txt') as f:
    words = f.read().splitlines()

for word in words:
    if check_word(word):
        print(f"Found a matching word: {word.upper()}")
