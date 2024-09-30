class Renderer:
    """Responsible for rendering information about the game in the console.

    Attributes:
        __CONSOLE_HANGMAN_PICTURES: List of sprites of various hangman_game states.
    """
    __CONSOLE_HANGMAN_PICTURES: list[str] = [
        """ 
        ----------
        |        |
        |        
        |
        |
        |_________ 
        """,
        """ 
        ----------
        |        |
        |        0
        |
        |
        |_________ """,
        """ 
        ----------
        |        |
        |        0
        |        |
        |
        |_________ """,
        """ 
        ----------
        |        |
        |        0/
        |        |
        |
        |_________ """,
        """
        ----------
        |        |
        |       \\0/
        |        |
        |
        |_________ """,
        """
        ----------
        |        |
        |       \\0/
        |        |
        |       /
        |_________ """,
        """
        ----------
        |        |
        |       \\0/
        |        |
        |       / \\
        |_________ """,
    ]

    def render(self, attempts: int, word: str, user_letters: set[str]) -> None:
        """
        Renders information to the player every turn.

        :return: None.
        """
        print(self.get_sprite_for_hangman(attempts))
        print(f"Текущее слово {word}\n"
              f"Попытка: {attempts}\n"
              f"Использованные буквы: {user_letters}")

    def get_sprite_for_hangman(self, attempts: int) -> str:
        """
        Returns a specific hangman_game's sprite depending on the player's condition
        (number of attempts).

        :param attempts: The number of attempts made by the player
        :return: Hangman's sprite.
        """
        return self.__CONSOLE_HANGMAN_PICTURES[attempts]
