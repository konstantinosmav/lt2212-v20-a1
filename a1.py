import os
import sys
from collections import Counter
import pandas as pd
import numpy as np
import numpy.random as npr

def load_dict_of_dirs(dir1, dir2):
    """Creates a dictionary where the key is the filename and the value is every article in the form of a list
    containing the terms as strings"""
    
    d1 = glob.glob('{}/*.txt'.format(dir1))
    d2 = glob.glob('{}/*.txt'.format(dir2))
    d1_and_d2 = d1
    d1_and_d2 += d2
    dict_of_dirs = {}
    for filename in d1_and_d2:
        words = []
        with open(filename, "r") as f:
            for line in f.readlines():
                words += [word.lower() for word in line.split() if word.isalpha()]
                dict_of_dirs[filename] = words
    return dict_of_dirs
    

def count_unique_words(dir1, dir2):
    directories = load_dict_of_dirs(dir1, dir2)
    
    list_of_counts = []
    for item in directories.items():
        full_file_path = item[0]

        split_path = full_file_path.split('\\')
        file_name = split_path[-1]
        direc_name = '\\'.join(split_path[:-1])
        words = item[1]
        count_of_words = Counter(words)
        #print(count_of_words)
            
        count_dict = {}
        count_dict['directory'] = direc_name
        count_dict['file_name'] = file_name
        
        
        count_dict.update(count_of_words)
        list_of_counts.append(count_dict)
        #print(count_dict)
    return list_of_counts
       
def get_unique_words(dir1, dir2):
    directories = load_dict_of_dirs(dir1, dir2)
    list_of_all_words = []
    
    for item in directories.items():
        words =item[1]
        for w in words:
            list_of_all_words.append(w)
            #print(list_of_all_words)
    set_of_words = sorted(set(list_of_all_words))
    return set_of_words
        

    

def part1_load(dir1, dir2, n=1):
    counted_words = count_unique_words(dir1, dir2)
    unique_words = get_unique_words(dir1, dir2)
    
    data_frame = pd.DataFrame(counted_words)
    data_frame[unique_words] = data_frame[unique_words].replace(np.nan, 0)   
    
    for column in data_frame[unique_words]:
        times_of_occurrence = data_frame[column].sum()
        if n >= times_of_occurrence:
            del data_frame[column]
            
    return data_frame
    
def part2_vis(df, m):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)
    grouped_and_transposed_df = df.groupby(by=["directory"], sort=True).sum().T
    print(grouped_and_transposed_df)

# ADD ANY OTHER IMPORTS YOU LIKE



def part3_tfidf(df):
    # DO NOT CHANGE
    assert isinstance(df, pd.DataFrame)

    # CHANGE WHAT YOU WANT HERE
    return df #DUMMY RETURN

# ADD WHATEVER YOU NEED HERE, INCLUDING BONUS CODE.
