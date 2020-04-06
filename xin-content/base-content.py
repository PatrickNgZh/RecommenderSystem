import pandas as pd
import numpy as np

# favourite_list = pd.read_csv('favourite_list.csv',skiprows=355914,header=None,names=['user_id','playlist_id','playlist_name','song_id','song_name','tag_count'])

favourite_list = pd.read_csv('favourite_list.csv',nrows=355912)
print(favourite_list.tail())
print(favourite_list.shape)
print(favourite_list.info())

user1 = favourite_list[favourite_list['user_id'] == 575288905]
print(user1.shape)
print(user1.info())

# print(user1.head())

# print(user1['song_tag'])


## extract the user tag on favorite
user1_tag = {}
for i, tag in user1['song_tag'].items():
    if tag in user1_tag:
        user1_tag[tag] += int(user1.loc[i]['tag_count'])
    elif tag != '\\N':
        user1_tag[tag] = int(user1.loc[i]['tag_count'])

user1_tag = sorted(user1_tag.items(), key=lambda x:x[1], reverse=True)
print(user1_tag)
print('======================\n')

# extract the user history songs rank_list

rank_list = pd.read_csv('ranklist.csv')
# print(rank_list.shape)
# print(rank_list.head())
# print(rank_list.info())

user2 = rank_list[rank_list['user_id'] == 1313848989]
print(user2.shape)
print(user2.head())
print(user2.info())
# print(user2)

user2_tag = {}
for i, tag in user2['song_tag'].items():
    if tag in user2_tag:
        user2_tag[tag] += int(user2.loc[i]['tag_count'])
    elif tag != '\\N':
        user2_tag[tag] = int(user2.loc[i]['tag_count'])

user2_tag = sorted(user2_tag.items(), key=lambda x:x[1], reverse=True)
print(user2_tag)