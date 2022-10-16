'''
This script combines all of the csv files that contain the YouTube metadata
I combined 100 files, leaving a csv file with metadata for over 50k videos
'''
# https://stackoverflow.com/questions/41857659/python-pandas-add-filename-column-csv

import pandas as pd
import glob
import os

#creates a list of all csv files in the current folder
globbed_files = glob.glob("*.csv")

# pd.concat takes a list of dataframes as an agrument
data = []

for csv in globbed_files:
    frame = pd.read_csv(csv)
    # https://stackoverflow.com/questions/46449408/removing-file-extension-from-filename-with-file-handle-as-input
    # add a column containing the search term trigram (taken from the csv filename)
    frame['trigram'] = os.path.splitext(os.path.basename(csv))[0]
    data.append(frame)

# this df will have the original index and the new index for this def
# maybe this is useful, or I could always delete the column later
bigframe = pd.concat(data, ignore_index=True) #dont want pandas to try an align row indexes
bigframe.to_csv("random_trigrams_bigdata.csv", encoding='utf8')
