import sys
import codecs
import logging


class FileManager:
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s : {app.%(funcName)s} %(message)s', level=logging.INFO)

    @staticmethod
    def parse_data_from_files():
        logging.info("Checking for filepaths in the command line arguments.")
        # List sliced, since sys.argv[0] is "main.py"
        resultant_highest_occurrences_number = int(sys.argv[1])
        filepaths = sys.argv[2:]
        contents_of_files = []

        # For reasons of consistency, the condition has been written in
        # such a way that only either of the two commands may be used,
        # but not a combination of the two -

        # python main.py test-files/sample.txt test-files/sample_two.txt
        # cat sample_two.txt | python main.py

        if not filepaths:
            # If the Command Line Arguments succeeding "main.py" have no filepaths,
            # perform the following.
            logging.info("No filepaths found in the command line arguments.")
            logging.info("Checking for any text given as input using 'cat'.")

            resultant_line = ''
            for line in sys.stdin:
                resultant_line += line

            # Explicitly decoding escape characters, since file read is not performed
            # by Python when it receives an input from 'cat filename.txt'
            contents_of_files.append(codecs.decode(
                resultant_line, "unicode_escape"))
            logging.info(
                f"Parsing data from the pipelined input text successful.")

        else:
            # If the Command Line Arguments succeeding "main.py" have filepaths,
            # perform the following.
            logging.info(
                f"Found {len(filepaths)} files in the command line arguments.")

            for filepath in filepaths:
                logging.info(f"Parsing data from file at path '{filepath}'.")
                try:
                    file = open(filepath, "r", encoding='unicode_escape')
                except Exception as e:
                    if isinstance(e, FileNotFoundError):
                        logging.error(
                            f"No file exists with the name/path {filepath}.")
                        logging.error(
                            f"WARNING : Skipping this file, as it does not exist.")
                        continue
                file_content = file.read()
                contents_of_files.append(file_content)
                logging.info(f"Parsing data successful.")

        return resultant_highest_occurrences_number, contents_of_files
