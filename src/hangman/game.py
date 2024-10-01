from hangman.state import State
from hangman.renderer import Renderer
from hangman.word_manager import WordManager
from hangman.input_handler import InputHandler


class Game:
    """The main class that runs the Hangman game."""

    def __init__(
        self,
        state: State,
        renderer: Renderer,
        word_manager: WordManager,
        input_handler: InputHandler,
    ):
        self._attempts: int = 0
        self._player_word: str = ""
        self._used_letters: list[str] = []
        self._state = state
        self._renderer = renderer
        self._word_manager = word_manager
        self._input_handler = input_handler
        self._words = self._word_manager.get_words_from_file()

    def start(self) -> None:
        """Launches the main game loop."""
        self._input_handler.set_renderer(self._renderer)
        self._renderer.display_game_options()
        player_input: str = self._input_handler.get_player_input()

        while not self._state.is_finish_game(player_input):
            if self._state.is_start_game(player_input):
                self._renderer.diplay_start_game_message()
                self.loop()
            player_input = self._input_handler.get_player_input()

        self._renderer.display_finish_game_state()

    def loop(self) -> None:
        """The main game loop."""
        secret_word: str = self._word_manager.get_random_word(self._words)
        self._player_word = "*" * len(secret_word)
        self._used_letters.clear()
        self._attempts = 0

        while not self._state.is_game_over(self._attempts):
            self._renderer.dipplay_current_state(
                self._attempts, self._player_word, self._used_letters
            )

            if self._state.is_game_won(secret_word, self._player_word):
                self._renderer.display_win_message(self._attempts)
                break

            player_input = self._input_handler.get_player_input()

            self._make_move(secret_word, player_input)
        else:
            self._renderer.display_lose_message(secret_word, self._attempts)
            self._renderer.display_game_options()

    def _make_move(self, secret_word: str, player_input: str) -> None:
        if player_input not in self._used_letters:
            if player_input in secret_word:
                self._used_letters.append(player_input)
                self._player_word = self._update_player_word(secret_word, player_input)
            else:
                self._attempts += 1
                self._used_letters.append(player_input)
        else:
            self._renderer.display_letter_used_message(player_input)

    def _update_player_word(self, secret_word: str, player_input: str):
        return "".join(
            [
                letter if letter == player_input else self._player_word[i]
                for i, letter in enumerate(secret_word)
            ]
        )
