from hangman.game import Game
from hangman.state import State
from hangman.renderer import Renderer
from hangman.word_manager import WordManager
from hangman.input_handler import InputHandler


def main() -> None:
    path: str = "data/ru_words.txt"
    lose_state: int = 6
    valid_letters: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    renderer = Renderer()
    game = Game(
        State(lose_state),
        renderer,
        WordManager(path),
        InputHandler(renderer, valid_letters),
    )
    game.start()


if __name__ == "__main__":
    main()
