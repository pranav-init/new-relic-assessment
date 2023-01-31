import logging


class ContentPreprocessor:
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s : {app.ContentPreprocessor.%(funcName)s} %(message)s', level=logging.INFO)

    punctuation_marks = '''!()-[]{};:'"“”’\,<>./?@#$%^&*_~'''

    @staticmethod
    def preprocess_content(text: str) -> str:
        list_of_words = text.split()
        for index in range(len(list_of_words)):
            current_word = list_of_words[index]
            current_word_without_punctuation: str = ''
            for character in current_word:
                if character not in ContentPreprocessor.punctuation_marks:
                    # Add the character to the final string, only if it
                    # is not a punctuation mark.
                    current_word_without_punctuation += character

            # Converting the word into lowercase, to make it case insensitive
            current_word = current_word_without_punctuation.lower()
            list_of_words[index] = current_word

        logging.info(
            "Successfully removed case, punctuation marks from the words in the current file.")
        return list_of_words
