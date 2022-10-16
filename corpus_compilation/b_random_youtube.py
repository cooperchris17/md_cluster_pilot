from apiclient.discovery import build
from bnc_seeds import bnc_200_words
import pandas as pd
import random

# you need to register an API key (https://developers.google.com/youtube/v3/getting-started)
api_key = 'INPUT_API_KEY'
# generate a random trigram from the frequent BNC (200) words
tri_gram = ' '.join(random.sample(bnc_200_words, 3))
# use the trigram as a search term
search_term = tri_gram

youtube = build('youtube', 'v3', developerKey=api_key)

# create an empty list to extract the video information to
videos = [ ]

# nextPageToken is necessary to extract more than 50 maxResults
# this while loop will search for the maximum number of videos that fit the search parameters
# maximum = 500-600
nextPageToken = None
while 1:
    res = youtube.search().list(q=search_term,
                part='id, snippet',
                type='video', videoDuration='medium', relevanceLanguage='en',
                publishedAfter='2021-01-01T00:00:00Z', publishedBefore='2021-12-31T23:59:59Z',
                maxResults=50, pageToken=nextPageToken).execute()

    videos += res["items"]
    nextPageToken = res.get("nextPageToken")
    if nextPageToken is None:
        break

#create an empty list for each column of metadata
video_id = [ ]
title = [ ]
published_at = [ ]
channel_title = [ ]
channel_id = [ ]
description = [ ]
etag = [ ]

# for each video, append the list with the information
for i in range(len(videos)):
    video_id.append((videos[i])['id']['videoId'])
    title.append((videos[i])['snippet']['title'])
    published_at.append((videos[i])['snippet']['publishedAt'])
    channel_title.append((videos[i])['snippet']['channelTitle'])
    channel_id.append((videos[i])['snippet']['channelId'])
    description.append((videos[i])['snippet']['description'])
    etag.append((videos[i])['etag'])

# create a dictionary
data = {'video_id': video_id,'title': title, 'published_at': published_at,
        'channel_title':channel_title,'channel_id':channel_id,
        'description':description, 'etag':etag}

# convert to dataframe and output to a csv file (name specified by 'channel_name' above)
df = pd.DataFrame(data)
search_term_for_file = search_term.replace(' ', '_')
csv_file = search_term_for_file+'_medium.csv'
df.to_csv(csv_file, encoding='utf8')
# print the df to look at the data and see how much has been extracted
print(df)


