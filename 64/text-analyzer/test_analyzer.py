from analyzer import (
    count_words,
    count_characters,
    count_vowels,
    reverse_text
)


def test_count_words():
    assert count_words("Hello world Python") == 3


def test_count_characters():
    assert count_characters("Hello world") == 11


def test_count_vowels():
    assert count_vowels("Hello World") == 3


def test_reverse_text():
    assert reverse_text("Python") == "nohtyP"