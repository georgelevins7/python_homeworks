def count_words(text):
    return len(text.split())


def count_characters(text):
    return len(text)


def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)


def reverse_text(text):
    return text[::-1]