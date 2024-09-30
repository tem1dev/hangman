from random import choice


class RandomWord:
    """Uses method that returns random word from list of words."""

    def __init__(self, words: list[str]) -> None:
        """Initialization RandomWord object.

        :param words: The list of words for random choice."""
        self.words = words

    def get_random_word(self) -> str:
        """
        Choices random word from list of words and returns it.

        :return: Random word.
        """
        return choice(self.words)
