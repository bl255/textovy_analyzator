# Textový analyzátor
#### Text Analyser

### Introduction
This is a simple python program created as the first assignment for [Engeto](https://engeto.cz/) Python Academy.

### Functionality
The task was to create a program which:
* takes username and password and compares them to the user data
* lets the user choose from the available texts
* prints the overall word count, count of titlecase words, count of lowercase words, count of uppercase words, count of numeric strings, the sum of numeric strings
* prints the number of words for every word length and a simple chart of the word count frequency

### Added Functionality - Language Choice
I added the choice of the language at the beginning of the program run.
* 'en': English
* 'cz': Czech
* 'sk': Slovak

Based on the user choice, the text strings for inputs and print statements are imported from the respective python files in the languages' directory.

### Structure
* [projekt_1.py](projekt_1.py) - the main file for running the program
* [languages](/languages) - the directory with python files [en.py](languages/en.py), [cz.py](languages/cz.py), [sk.py](languages/sk.py) which contain the text strings for the language mutations
* [registered_users.txt](registered_users.txt) - user data as a .txt file, each row is in the format: 'username,password'
* [task_template.py](task_template.py) - includes 'TEXTS' list of the texts

### Final Thoughts
I created the 'print_line_separator' and 'print_table_line' functions  for the final table print, but I might implement [prettytable](https://pypi.org/project/prettytable/) python module for the table print in the future.
