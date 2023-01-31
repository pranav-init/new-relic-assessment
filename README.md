### Introduction

This repository explains the solution to the three-word-sequence-count problem, as part of my New Relic Coding Assessment. I would highly recommend you to watch [this recording](https://www.loom.com/share/7dc5a1343cb5451ea57adc2e302ed161), as it includes
- a briefing of the solution and the modules used, which would help you navigate through this repository
- a briefing of the tests performed, the commands used and the text files used to test the solution

### Testing The Code 

The file ```main.py``` needs to be run with the required text files in the command line arguments, in order to enable the Python program to accept these as inputs, and accordingly, parse data from them. To do this, the two ways as described in the problem statement are as follows - 

##### Using the 'cat' Command To Pipeline The Output Into The Python Program
```
cat test-files/sample.txt | python main.py
```

##### Specifying The Input Files In Command Line Arguments 
```
python main.py test-files/sample.txt test-files/sample_two.txt test-files/sample_three.txt
```
### Sample Output

![image](https://user-images.githubusercontent.com/84697979/215775509-088e4a9c-bd69-4100-b1ea-0331150b35b9.png)


### Explanation Of The Modules Used
The file ```main.py``` depends on three modules - 
1. **FileManager**, which decodes the command given in the terminal, extracts files from the same, reads contents of all of these files, and returns a list of contents of all of the files given as input.
2. **OccurrenceAnalyzer**, which parses the words and characters of the contents of each of the files in the aforementioned list, identifies three word sequences, keeps track of the count of each of these sequences in a dictionary, sorts them based on occurrences and displays the same.
3. **ContentPreprocessor**, which is a dependency consumed by **OccurrenceAnalyzer**, and primarily deals with breaking down the contents of a file into words, removing punctuation marks from these words and converting them into lowercase.
