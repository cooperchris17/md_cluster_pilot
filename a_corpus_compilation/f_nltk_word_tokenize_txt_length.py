'''
For all txt files in the folder:
the texts are tokenized with NLTK word_tokenize (they'll -> 'they', "'ll" / can't -> 'ca', "n't" / possesive 's' counted as token)
then punctuation tokens are deleted -> '.', ',', '-', '?'
then the tokens in each text are counted + mean and sd
'''

from nltk.tokenize import word_tokenize
import glob, os
import numpy as np
import pandas as pd

text_lengths = []
# read all the txt files in the directory (and in other directories in that path)
for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            f = open(file, "r")
            raw = f.read()
                    
            tokens = word_tokenize(raw)
            # I only added these punctuation marks as I know which ones are in the texts from pre-processing ('.', ',', '?')
            # '-' has been added to account for hyphenated words
            sent_punc = {'.', ',', '-', '?'}
            no_punc_tokens = [token.lower() for token in tokens if token not in sent_punc]

            text_lengths.append(len(no_punc_tokens))

print('descriptive statistics for text length:')
# pandas describe - it uses the sample sd  - be comparison numpy uses population sd
text_length_series = pd.Series(text_lengths)
print(text_length_series.describe().round(2))
print('')
print('number of tokens in corpus: ', sum(text_lengths))
