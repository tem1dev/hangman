import random


class WordManager:
    """A class designed to read a file."""

    def __init__(self, path_to_file: str):
        self._path_to_file = path_to_file

    def get_words_from_file(self) -> list[str]:
        """Reads words from file and returns them as a list."""
        try:
            with open(self._path_to_file, "r", encoding="utf-8") as f:
                words = [word.strip() for word in f]
            return words
        except FileNotFoundError:
            raise FileNotFoundError(f"File {self._path_to_file} not found")
        except Exception as e:
            raise RuntimeError(f"An error occurred {e}")

    def get_random_word(self, words: list[str]) -> str:
        """Returns random word from list of words"""
        return random.choice(words)
