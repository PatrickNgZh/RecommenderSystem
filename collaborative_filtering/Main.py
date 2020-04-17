import heapq

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def calculate_rating(a, b, c, b1, c1):
    rating = np.mean(a)
    user1 = calculate_consin(a, b) * (b1 - rating)
    user2 = calculate_consin(a, c) * (c1 - rating)
    rating = rating + ((user1 + user2) / (calculate_consin(a, b) + calculate_consin(a, c)))
    return rating


def calculate_consin(a, b):
    temp = np.linalg.norm(a) * np.linalg.norm(b)
    if temp == 0:
        return 0
    else:
        return np.dot(a, b) / temp


def data_preprocess(path):
    df = pd.read_csv(path)
    users = dict()
    for row in df.iterrows():
        if row[1]['userid'] not in users:
            users[row[1]['userid']] = dict()
        if row[1]['song_id'] not in users[row[1]['userid']]:
            users[row[1]['userid']][row[1]['song_id']] = row[1]['song_score']
    return pd.DataFrame(users).T, users.keys()


def recommend(path, user_id):
    df, users = data_preprocess(path)
    df = df.fillna(0)
    songs = df.columns.values
    users = list(users)

    data = df.to_numpy()
    estimator = KMeans(n_clusters=5)
    results = estimator.fit(data)
    labels = results.labels_
    index = users.index(user_id)
    flag = labels[index]

    similarity = list()
    for i, value in enumerate(labels):
        if i == index or flag != labels[index]:
            continue
        else:
            temp = calculate_consin(data[index], data[i])
            if temp == 1:
                similarity.append(0)
            else:
                similarity.append(temp)

    max_num_index_list = map(similarity.index, heapq.nlargest(2, similarity))
    max_num_index_list = list(max_num_index_list)

    candidates = list()
    for col in range(len(songs)):
        if data[max_num_index_list[0]][col] != 0 or data[max_num_index_list[1]][col] != 0 and data[index][col] == 0:
            candidates.append(col)

    ratings = list()
    lut = list()
    for i, song_index in enumerate(candidates):
        lut.append(song_index)
        ratings.append(calculate_rating(data[index], data[max_num_index_list[0]], data[max_num_index_list[1]]
                                        , data[max_num_index_list[0]][song_index],
                                        data[max_num_index_list[1]][song_index]))

    recommend_song_list = map(ratings.index, heapq.nlargest(5, ratings))
    recommend_song_list = set(recommend_song_list)


    recommend_list = list()
    for song_index in recommend_song_list:
        recommend_list.append(songs[lut[song_index]])

    return recommend_list


if __name__ == '__main__':
    print(recommend('music_record.csv', 1999616317))
