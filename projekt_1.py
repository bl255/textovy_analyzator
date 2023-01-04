import sys
import re
from collections import Counter
from importlib import import_module
from task_template import TEXTS

NOR_COL = 16
PRINT_WIDTH = 64


def print_line_separator(num=PRINT_WIDTH):
    print("-" * num)


def print_table_line(row_list, col_width=NOR_COL):
    print("".join((item.ljust(col_width) for item in map(str, row_list))))


# CHOOSING LANGUAGE
lang = import_module(f'languages.{input("Language/Jazyk (en, cz, sk): ")}')

# USER VERIFICATION
user_name = input(lang.t_uname_input)
users_input = "registered_users.txt"

with open(users_input, mode="r") as text_file:
    for line in text_file:
        if line.strip().split(",")[0] == user_name:
            user = line.strip().split(",")
            break
        else:
            user = None

if not user:
    print(lang.t_uname_error)
    sys.exit()

user_password = input(lang.t_password_input)

if user_password != user[1]:
    print(lang.t_password_error.format(user_name=user_name))
    sys.exit()

# TEXT CHOICES
num_of_texts = len(TEXTS)
if TEXTS:
    text_choices = lang.t_text_choice.format(num_of_texts=num_of_texts)
else:
    text_choices = lang.t_no_text

# PRINTING WELCOME AND TEXT CHOICES
print_line_separator()
print(lang.t_wellcome.format(user_name=user_name, text_choices=text_choices))
print_line_separator()

# CHOOSING TEXT
chosen_text_num = input(lang.t_text_num.format(num_of_texts=num_of_texts))
if not chosen_text_num.isnumeric():
    print(lang.t_not_num)
    sys.exit()
treated_num = int(chosen_text_num) - 1
if treated_num not in range(num_of_texts):
    print(lang.t_not_in_range)
    sys.exit()
text = TEXTS[treated_num]
print_line_separator()

# ANALYSING THE TEXT
text_list = re.findall(r"\w+", text)
anl = {"all": len(text_list),
       "title": sum((w.istitle() for w in text_list if not w.isupper())),
       "upper": sum((w.isupper() for w in text_list)),
       "lower": sum((w.islower() for w in text_list)),
       "digits": sum((w.isnumeric() for w in text_list)),
       "sum_numbers": sum((int(w) for w in text_list if w.isnumeric()))}

# PRINTING THE TEXT ANALYSIS
print(lang.t_anl.format(*anl.values()))

# CALCULATING THE WORDS LENGTHS
text_lengths = sorted(Counter(map(len, text_list)).items())

# PRINTING WORDS LENGTHS AND LENGTHS CHART
print_line_separator()
print_table_line(lang.t_col_names)
print_line_separator()
for le, occur in text_lengths:
    prc = occur / anl["all"] * 100
    line = [le, occur, round(prc, 2), round(prc) * '*']
    print_table_line(line)

# TODO readme
# TODO skontroluj gramatku
