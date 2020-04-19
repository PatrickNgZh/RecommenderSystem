from my_tools.logger_tool import loggler_tool
import os
import sys
from my_tools.database_tool import database_tool
import pandas
import numpy

logger = loggler_tool()


def get_existed_favourite_list(user_id=1493673206):
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
 
def get_existed_ranklist(user_id=1493673206):
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
 

def get_existed_music_records(user_id=1493673206):
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
 
#test
# favourite_list=get_existed_favourite_list()
# music_record = get_existed_music_records()
# rank_list=get_existed_ranklist()
# print(rank_list.head())


##### for code start

favourite_sql="SELECT  f.user_id AS user_id, f.playlist_id AS playlist_id,  f.playlist_name AS playlist_name, g.song_id AS song_id, h.song_name AS song_name, j.artist_name AS artist_name, i.tag_name AS tag_name, i.tag_count AS tag_count FROM (select * from (SELECT a.user_id AS user_id, b.playlist_id AS playlist_id,  c.playlist_name AS playlist_name, d.tag_name AS tag_name from user a left join user_playlist b on a.user_id=b.user_id  left join playlist c on b.playlist_id=c.playlist_id  left join playlist_tag d on c.playlist_id=d.playlist_id) e where tag_name is NULL) f  left join song_playlist g on f.playlist_id=g.playlist_id left join artist_song l on l.song_id=g.song_id left join artist j on l.artist_id = j.artist_id left join song h on g.song_id = h.song_id left join song_tag i on i.song_id= h.song_id where h.song_name is not null and h.song_name <> '' and j.artist_name is not null and j.artist_name <> '' and i.tag_count > 1 and f.playlist_name like '%喜欢的音乐' and f.user_id={}"
rankllist_sql="SELECT  a.user_id AS user_id, b.ranklist_id AS ranklist_id, c.song_id AS song_id, c.song_score AS song_socre, e.song_name AS song_name, h.artist_name AS artist_name, d.tag_name AS tag_name, d.tag_count  AS tag_count from user a left join user_ranklist b on a.user_id=b.user_id  left join song_ranklist c on b.ranklist_id = c.ranklist_id  left join artist_song g on c.song_id=g.song_id left join artist h on g.artist_id = h.artist_id left join song_tag d on c.song_id=d.song_id  left join song e on d.song_id=e.song_id where d.tag_count >1 and e.song_name is not null and e.song_name <> '' and h.artist_name is not null and h.artist_name <> ''  and a.user_id={}"
musicrecord_sql="SELECT  a.user_id AS userid, b.ranklist_id AS ranklistid, c.song_id AS song_id, c.song_score AS song_socre, e.song_name AS song_name, h.artist_name AS artist_name from user a left join user_ranklist b on a.user_id=b.user_id  left join song_ranklist c on b.ranklist_id = c.ranklist_id  left join song e on c.song_id=e.song_id left join artist_song g on c.song_id=g.song_id left join artist h on g.artist_id = h.artist_id where e.song_name is not null and e.song_name <> '' and h.artist_name is not null and h.artist_name <> '' and c.song_score>1 and a.user_id={}"

def code_favourite_list(user_id=1493673206):
    # favourite_lists = database_tool().execute(
    #     sql="select * from recomend_favourite",execute_type=1, return_type=2
    # )
    # for target user
    # user_id='1493673206'
    favourite_lists = database_tool().execute(
            sql=favourite_sql.format(user_id),execute_type=1, return_type=2
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
 
def code_ranklist(user_id=1493673206):
    # favourite_lists = database_tool().execute(
    #     sql="select * from recomend_favourite",execute_type=1, return_type=2
    # )

    ranklists = database_tool().execute(
            sql=rankllist_sql.format(user_id),execute_type=1, return_type=2
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
 

def code_music_records(user_id=1493673206):
    records_lists = database_tool().execute(
        sql=musicrecord_sql.format(user_id),execute_type=1, return_type=2
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

code_favourite_list=code_favourite_list()
code_ranklist = code_ranklist()
code_music_record=code_music_records()
print(code_favourite_list.head())