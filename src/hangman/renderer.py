from typing import Final

CONSOLE_HANGMAN_PICTURES: Final[list[str]] = [
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


class Renderer:
    """Responsible for rendering information about the game in the console."""

    def dipplay_current_state(
        self, attempts: int, word: str, used_letters: list[str]
    ) -> None:
        """Renders information to the player every turn."""
        print(self.get_sprite_for_hangman(attempts))
        print(
            f"Текущее слово {word}\n"
            f"Неудачных попыток: {attempts}\n"
            f"Использованные буквы: {used_letters}"
        )

    def display_game_options(self) -> None:
        print("Вам доступны две опции: начать или завершить игру (Д/н)")

    def display_lose_message(self, secret_word: str, attempts: int) -> None:
        print(self.get_sprite_for_hangman(attempts))
        print(f"К сожалению вы проиграли. Загаданное слово: {secret_word}.\n")

    def diplay_start_game_message(self) -> None:
        print("Игра началась. Попробуйте угадать слово!")

    def display_win_message(self, attempts: int) -> None:
        print(f"Поздравляем, вы победили! Неудачных попыток: {attempts}.")

    def display_letter_used_message(self, letter: str) -> None:
        print(f"Букву '{letter}' вы уже использовали. Попробуйте снова.")

    def display_enter_message(self) -> None:
        print("Введите текст (букву):", end=" ")

    def display_incorrect_input_message(self) -> None:
        print("Неверный ввод. Попробуйте снова.")

    def display_finish_game_state(self) -> None:
        print("Вы завершили игру.")

    def get_sprite_for_hangman(self, attempts: int) -> str:
        return CONSOLE_HANGMAN_PICTURES[attempts]
