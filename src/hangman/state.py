class State:
    """Contains predicate methods that check a certain state of the game."""

    def __init__(self, lose_state):
        self._lose_state = lose_state

    def is_game_won(self, secret_word: str, player_word: str) -> bool:
        return secret_word == player_word

    def is_game_over(self, attempts: int) -> bool:
        return attempts == self._lose_state

    def is_finish_game(self, line: str) -> bool:
        return line.startswith("н")

    def is_start_game(self, line: str) -> bool:
        return line.startswith("д")
