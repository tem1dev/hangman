class FileReader:
    """A class designed to read a file."""

    @staticmethod
    def get_words_from_file(path: str) -> list[str]:
        """
        Reads words from file and returns them as a list.

        :param path: The path to the file with words.
        :return:     The list of words.
        :raises      FileNotFoundError: If the file is not found.
        :raises      RuntimeError: If an error occurs while reading the file.
        """
        try:
            with open(path, encoding="utf-8") as f:
                words = [word.strip() for word in f]
            return words
        except FileNotFoundError:
            raise FileNotFoundError(f"File {path} not found")
        except Exception as e:
            raise RuntimeError(f"An error occurred {e}")
