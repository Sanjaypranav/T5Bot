#Reading text files to convert to df
import os 
import pandas as pd

def read_text_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

# read odd line texts from a text file 
def read_odd_lines(filepath):
    with open(filepath, "r") as f:
        return [line for i, line in enumerate(f) if i % 2 == 0]

# read even line texts from a text file
def read_even_lines(filepath):
    with open(filepath, "r") as f:
        return [line for i, line in enumerate(f) if i % 2 != 0]


