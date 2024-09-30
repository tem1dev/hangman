from hangman.file_management.file_reader import FileReader
from hangman.game_state.state import State
from hangman.user_input.player_input import PlayerInput
from hangman.display.renderer import Renderer
from hangman.word_selection.random_word import RandomWord


class Game:
    """The main class that runs the Hangman game."""
    WORDS_FILE_PATH: str = "data/ru_words.txt"

    def __init__(self) -> None:
        """
        Initialization Hangman object.

        This method sets the initial attributes of the game, creates instances of the class
        necessary for correct operation.

        Attributes
            __attempts: The number of attempts made by the player.
            __used_letters: Set of used letters.
            __player_word: The word that player guesses opens with each guessed letter.
            __state: Instance of class State, uses methods related to the player's condition.
            __player_input: Has a method that additionally validates user input.
            __rendered: It is used to render each step.
            __random_word: Reads words from a file and uses a method to output a random word.

        Notes:
            The path to the file is set by the WORDS_FILE_PATH variable.
        """
        self.__attempts: int = 0
        self.__used_letters: list[str] = []
        self.__player_word: str | None = None
        self.__state: State = State()
        self.__player_input: PlayerInput = PlayerInput()
        self.__renderer: Renderer = Renderer()
        self.__random_word: RandomWord = RandomWord(FileReader.get_words_from_file(self.WORDS_FILE_PATH))

    def start(self) -> None:
        """Launches the main game loop."""
        self.loop()

    def loop(self) -> None:
        """
        The main game loop.

        :return: None.
        """
        while True:
            user_input: str = self.__player_input.get_user_input("Начать игру или завершить [Д/н]")
            if self.__state.is_finish_game(user_input):
                break
            if not self.__state.is_start_game(user_input):
                continue
            secret_word: str = self.__random_word.get_random_word()
            self.__player_word = '*' * len(secret_word)
            self.__used_letters.clear()
            self.__attempts = 0

            while True:
                if self.__state.is_game_won(secret_word, self.__player_word):
                    print("Вы отгадали слово. Поздравляю.")
                    break
                elif self.__state.is_game_over(self.__attempts):
                    print(f"Вы потратили максимальное число попыток. Загаданное слово: {secret_word}")
                    self.__renderer.render(self.__attempts, self.__player_word, self.__used_letters)
                    break
                self.__renderer.render(self.__attempts, self.__player_word, self.__used_letters)
                user_input = self.__player_input.get_user_input()
                if user_input in secret_word and user_input not in self.__used_letters:
                    self.__update_player_word(secret_word, user_input)
                    self.__used_letters.append(user_input)
                elif user_input in self.__used_letters:
                    print("Буква уже использовалась. Попробуйте снова.")
                else:
                    self.__used_letters.append(user_input)
                    self.__attempts += 1

    def __update_player_word(self, secret_word: str, user_input: str) -> None:
        """
        A private method that is used to update the word by replacing the letters that the player guessed.

        :param secret_word: The encrypted word in which the letters open.
        :param user_input: The letter that player input.
        :return: None.
        """
        result = list(self.__player_word)
        for index, letter in enumerate(secret_word):
            if letter == user_input:
                result[index] = letter

        self.__player_word = "".join(result)
