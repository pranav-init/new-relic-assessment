from content_preprocessor import ContentPreprocessor
from typing import List, Tuple
import logging


class OccurrenceAnalyzer:
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s : {app.OccurrenceAnalyzer.%(funcName)s} %(message)s', level=logging.INFO)
    occurrence_pairs = {}

    @staticmethod
    def consolidate_occurrences_of_all_files(contents_of_files):
        for file_content in contents_of_files:
            OccurrenceAnalyzer.analyze_occurrences_per_file(file_content)

    @staticmethod
    def analyze_occurrences_per_file(file_content: str):
        list_of_words = ContentPreprocessor.preprocess_content(file_content)
        for index in range(len(list_of_words)-3):
            occurrence = f"{list_of_words[index]} {list_of_words[index+1]} {list_of_words[index+2]}"
            if occurrence not in OccurrenceAnalyzer.occurrence_pairs:
                OccurrenceAnalyzer.occurrence_pairs[occurrence] = 1
            else:
                OccurrenceAnalyzer.occurrence_pairs[occurrence] += 1
        logging.info("Occurrence pairing successful.")

    @staticmethod
    def render_occurrence_pairs() -> List[Tuple]:
        # Sorting the dictionary by value (i.e. number of occurrences)
        # via a list of tuples, sliced only to the first 100 elements.
        occurrence_pairs = sorted(OccurrenceAnalyzer.occurrence_pairs.items(),
                                  key=lambda tuple: tuple[1], reverse=True)[:100]

        logging.info(
            f"First {len(occurrence_pairs)} highest occurrences of three-word sequences :")
        for tuple in occurrence_pairs:
            print(f"{tuple[1]} - {tuple[0]}")
