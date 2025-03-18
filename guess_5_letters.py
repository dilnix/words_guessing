def check_word(word):
    excluded_letters = {'S', 'A', 'L', 'B', 'N', 'O'}
    required_letters = {'T', 'E', 'R'}

    if len(word) != 5:
        return False

    # Explicitly check each position
    if word[0] == 'r':
        return False

    # Explicitly check each position
    if word[1] in ['e', 't', 'r']:
        return False

    # Explicitly check each position
    if word[2] in ['e', 't']:
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
