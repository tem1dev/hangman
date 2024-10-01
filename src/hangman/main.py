from hangman.game import Game
from hangman.state import State
from hangman.renderer import Renderer
from hangman.word_manager import WordManager
from hangman.input_handler import InputHandler
from typing import Final

PATH: Final[str] = "data/ru_words.txt"


def main() -> None:
    game = Game(State(), Renderer(), WordManager(PATH), InputHandler())
    game.start()


if __name__ == "__main__":
    main()
