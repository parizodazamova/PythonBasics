# 1. given a phrase, count how many times each letter was used.
def count_letters(phrase):
    """
    Counts the occurrences of each letter in a given phrase and returns a dictionary.
    """
    letter_counts = {}
    for char in phrase.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.setdefault(char, 0) + 1
    return letter_counts

# 2. given a phrase, count how many times vowels( a, e, i, o, and u) were used.
def count_vowels(phrase):
    """
    Counts the occurrences of vowels ('a', 'e', 'i', 'o', 'u') in a given phrase.
    """
    vowels = set("aeiou")
    vowel_count = 0
    for char in phrase.lower():
        if char in vowels:
            vowel_count += 1
    return vowel_count

# Example usage
phrase = "Count vowels!"
letter_freq = count_letters(phrase)
print("Letter frequencies:", letter_freq)

vowel_count = count_vowels(phrase)
print("Vowel count:", vowel_count)