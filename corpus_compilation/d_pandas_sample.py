'''
To make the dataset smaller (and more manageable), but still retain 100 search terms, I sampled 5000 lines from the dataframe
This script randomly samples 5000 lines from the dig data metadata file using pandas
The output csv has no index column
'''

import pandas as pd
# read in the csv file
df = pd.read_csv('random_trigrams_bigdata.csv', index_col=0)
# change the number here to change the sample size
df2 = df.sample(n=5000)
# drop original index column (from original metadata dataframes)
df2.drop(df2.columns[0], axis=1, inplace=True)

# output the sample to a csv file
print(df2)
df2.to_csv('random_trigrams_5000_sample.csv', encoding='utf8', index=False)
