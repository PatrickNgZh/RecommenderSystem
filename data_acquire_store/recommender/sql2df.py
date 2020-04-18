from my_tools.logger_tool import loggler_tool
import os
import sys
from my_tools.database_tool import database_tool
import pandas
import numpy

logger = loggler_tool()

def get_favourite_list(user_id=1493673206):
    # favourite_lists = database_tool().execute(
    #     sql="select * from recomend_favourite",execute_type=1, return_type=2
    # )
    # for target user
    # user_id='1493673206'
    favourite_lists = database_tool().execute(
            sql="select * from recomend_favourite where user_id={}".format(user_id),execute_type=1, return_type=2
    )
    favourite_list_dict = {
        "user": [],
        "playlist": [],
        "playlist_name": [],
        "song_id":[],
        "song_name": [],
        "artist":[],
        "tag_name":[],
        "tag_count":[]
    }
    if favourite_lists[0]:
        for favourite in favourite_lists[1]:
                favourite_list_dict["user"].append(favourite[0])
                favourite_list_dict["playlist"].append(favourite[1])
                favourite_list_dict["playlist_name"].append(favourite[2])
                favourite_list_dict["song_id"].append(favourite[3])
                favourite_list_dict["song_name"].append(favourite[4])
                favourite_list_dict["artist"].append(favourite[5])
                favourite_list_dict["tag_name"].append(favourite[6])
                favourite_list_dict["tag_count"].append(favourite[7])
    
    data_frame = pandas.DataFrame(data=favourite_list_dict)
    return data_frame
 
def get_ranklist(user_id=1493673206):
    # favourite_lists = database_tool().execute(
    #     sql="select * from recomend_favourite",execute_type=1, return_type=2
    # )

    ranklists = database_tool().execute(
            sql="select * from recomend_ranklist  where user_id={}".format(user_id),execute_type=1, return_type=2
    )
    ranklist_dict = {
        "user": [],
        "ranklist_id": [],
        "song_id":[],
        "song_score":[],
        "song_name": [],
        "artist":[],
        "tag_name":[],
        "tag_count":[]
    }
    if ranklists[0]:
        for ranklist in ranklists[1]:
                ranklist_dict["user"].append(ranklist[0])
                ranklist_dict["ranklist_id"].append(ranklist[1])
                ranklist_dict["song_id"].append(ranklist[2])
                ranklist_dict["song_score"].append(ranklist[3])
                ranklist_dict["song_name"].append(ranklist[4])
                ranklist_dict["artist"].append(ranklist[5])
                ranklist_dict["tag_name"].append(ranklist[6])
                ranklist_dict["tag_count"].append(ranklist[7])
    
    data_frame = pandas.DataFrame(data=ranklist_dict)
    return data_frame
 

def get_music_records(user_id=1493673206):
    records_lists = database_tool().execute(
        sql="select * from recomend_musicrecord where userid={}".format(user_id),execute_type=1, return_type=2
    )
    music_record_dict = {
        "user": [],
        "song_id": [],
        "song_score": []
    }
    if records_lists[0]:
        for record in records_lists[1]:
                music_record_dict["user"].append(record[0])
                music_record_dict["song_id"].append(record[1])
                music_record_dict["song_score"].append(record[2])
    
    data_frame = pandas.DataFrame(data=music_record_dict)
    return data_frame
 
 
favourite_list=get_favourite_list()
music_record = get_music_records()
rank_list=get_ranklist()
print(rank_list.head())