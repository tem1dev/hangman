class PlayerInput:
    """It is a set of methods related to processing user input."""
    VALID_LETTERS: str = "абвгдежзийклмнопрстуфхцчщшъьэюя"
    VALID_INPUT_LENGTH: int = 1

    def get_user_input(self, text: str = "Ваш ввод") -> str:
        """
        Returns a single-character string entered by the user.

        :return: Character that user entered.
        """
        print(text)
        while not (self.is_valid_input(user_input := input())):
            print("Некорретный ввод. Попробуйте снова.")

        return user_input

    def is_valid_input(self, user_input: str) -> bool:
        """
        Returns true in the case of a valid character.

        :param user_input: Player input from the keyboard.
        :return: True or False depending on the validity of the input.
        """
        return len(user_input) == self.VALID_INPUT_LENGTH and user_input in self.VALID_LETTERS
