from occurrence_analyzer import OccurrenceAnalyzer
from file_manager import FileManager

# Step 1 : Data is parsed from the files given as input.
contents_of_files = FileManager.parse_data_from_files()

# Step 2 : The contents of all the obtained files are preprocessed,
# occurrences counted.
OccurrenceAnalyzer.consolidate_occurrences_of_all_files(contents_of_files)

# Step 3 : The resultant is printed.
OccurrenceAnalyzer.render_occurrence_pairs()
