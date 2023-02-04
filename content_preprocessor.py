import logging
import re


class ContentPreprocessor:
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s : {app.%(funcName)s} %(message)s', level=logging.INFO)

    @staticmethod
    def preprocess_content(text: str) -> str:
        text = re.sub(r'[^\w\s]', '', text).lower()
        list_of_words = text.split()
        logging.info(
            "Successfully removed case, punctuation marks from the words in the current file.")
        return list_of_words
