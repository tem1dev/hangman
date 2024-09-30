class State:
    """Contains predicate methods that check a certain state of the game.
    
    Attributes:
        __IS_LOSE_STATE: The number of attempts spent is equal to the loss.
    """
    __IS_LOSE_STATE = 6

    def is_game_won(self, secret_word: str, player_word: str) -> bool:
        """
        Checks if the player won.

        :param secret_word: The secret word from file.
        :param player_word: The word where the letters open while the player is guessing them.
        :return: True if player is won else False
        """
        return secret_word == player_word

    def is_game_over(self, attempts: int) -> bool:
        """
        Checks if the player has lost.

        :param attempts: Number of attempts made by player.
        :return: True if plyer has lost else False
        """
        return attempts == self.__IS_LOSE_STATE

    def is_finish_game(self, line: str) -> bool:
        """
        Checking whether to finish the game.

        :param line: Line input by player.
        :return: True if player wanted finish the game else False.
        """
        return line.lower().startswith('н')

    def is_start_game(self, line: str) -> bool:
        """
        Checking whether to start the game.

        :param line: Line input by player.
        :return: True if player wanted start the game else False.
        """
        return line.lower().startswith('д')