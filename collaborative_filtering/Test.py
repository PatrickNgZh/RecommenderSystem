import numpy as np


def get_average_ratings(matrix):
    dict = {}
    for i in range(matrix.shape[0]):
        sum = 0.0
        count = 0
        for j in matrix[i, :]:
            if j != 0:
                count += 1
            sum += j
        if count == 0:
            dict[i] = 0
        else:
            dict[i] = sum / count
    return dict


def calculate_consin(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def calculate_rating(a, b, c, b1, c1):
    rating = get_average_ratings(a)
    user1 = calculate_consin(a, b) * (b1 - rating)
    user2 = calculate_consin(a, c) * (c1 - rating)
    rating = (user1 + user2) / (calculate_consin(a, b) + calculate_consin(a, c))
    return rating
