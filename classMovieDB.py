import json
import requests
import urllib3
from classMovieDB import MovieDB

urllib3.disable_warnings()

proxie1s = {"https":"http://idalianis:idalianis@192.168.30.3:3128"}
db = MovieDB('https://34.240.190.150/', 'TestUser', 'ZfuzpbZ8Mo4' , proxie1s)
db.get_all()

action = input("Choose action: GET, POST, PUT, DELETE, PATCH or END to Exit.\n")
while action != "END":
    to_whom = input("Choose: ACTOR, DIRECTOR, MOVIE\n")
    if action == "GET":
        id_get = input("Which to return?\n")
        if to_whom == "ACTOR":
            db.get_actor(id_get)
        elif to_whom == "DIRECTOR":
            db.get_director(id_get)
        else:
            db.get_movie(id_get)
    elif action == "POST":
        if to_whom == "ACTOR":
            name_give = input("Give name.\n")
            birthday_give = input("Give birthday.\n")
            db.post_actor(name_give, birthday_give)
        elif to_whom == "DIRECTOR":
            name_give = input("Give name.\n")
            birthday_give = input("Give birthday.\n")
            db.post_director(name_give, birthday_give)
        else:
            name_give = input("Give name.\n")
            year_give = input("Give year.\n")
            dir_give = input("Give director id.\n")
            actor_list = list()
            flag = False
            while flag == False:
                actor_id = input('Actor of the new movie?(for exitting press OK.)\n')
                if actor_id == "OK":
                    flag=True
                else:
                    actor_list.append(actor_id)
            db.post_movie(name_give, year_give, dir_give, actor_list)
        db.get_all()
    elif action == "PUT":
        id_get = input("Which to update?\n")
        if to_whom == "ACTOR":
            name_give = input("Give new name.\n")
            birthday_give = input("Give new birthday.\n")
            db.put_actor(id_get, name_give, birthday_give)
        elif to_whom == "DIRECTOR":
            name_give = input("Give new name.\n")
            birthday_give = input("Give new birthday.\n")
            db.put_director(id_get, name_give, birthday_give)
        else:
            name_give = input("Give new name.\n")
            year_give = input("Give new year.\n")
            dir_give = input("Give new director id.\n")
            actor_list = list()
            flag = False
            while flag == False:
                actor_id = input('Actor of the movie?(for exitting press OK.)\n')
                if actor_id == "OK":
                    flag=True
                else:
                    actor_list.append(actor_id)
            db.put_movie(id_get, name_give, year_give, dir_give, actor_list)
        db.get_all()
    elif action == "PATCH":
        id_get = input("Which to update?\n")
        if to_whom == "ACTOR":
            name_give = input("Give new name.\n")
            db.patch_actor(id_get, name_give)
        elif to_whom == "DIRECTOR":
            name_give = input("Give new name.\n")
            db.patch_director(id_get, name_give)
        else:
            name_give = input("Give new name.\n")
            db.patch_movie(id_get, name_give)
        db.get_all()
    elif action == "DELETE":
        id_get = input("Which to delete?\n")
        if to_whom == "ACTOR":
            db.delete_actor(id_get)
        elif to_whom == "DIRECTOR":
            db.delete_director(id_get)
        else:
            db.delete_movie(id_get)
        db.get_all()
    else:
        print("Wrong action.\n")
    action = input("Choose action: GET, POST, PUT, DELETE or END to Exit.\n")
