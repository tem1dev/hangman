from typing import Final

IS_LOSE_STATE: Final[int] = 6


class State:
    """Contains predicate methods that check a certain state of the game."""

    def is_game_won(self, secret_word: str, player_word: str) -> bool:
        return secret_word == player_word

    def is_game_over(self, attempts: int) -> bool:
        return attempts == IS_LOSE_STATE

    def is_finish_game(self, line: str) -> bool:
        return line.startswith("н")

    def is_start_game(self, line: str) -> bool:
        return line.startswith("д")
