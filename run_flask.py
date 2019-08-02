import json
import requests
import urllib3
from MovieDB_flask import MovieDB
from flask import Flask , jsonify , request , flash
from flask_restful import Api , Resource

app=Flask(__name__)
api = Api(app)
urllib3.disable_warnings()
proxie1s = {"https":"http://idalianis:idalianis@192.168.30.3:3128"}
db = MovieDB('https://34.240.190.150/', 'TestUser', 'ZfuzpbZ8Mo4' , proxie1s)
db.get_all()

class Browser_requests():
    @app.route("/get/director/<int:id>", methods=['GET', 'POST'])
    def get_director(id):
        return(db.get_director(id))

    @app.route("/get/actor/<int:id>", methods=['GET', 'POST'])
    def get_actor(id):
        return(db.get_actor(id))

    @app.route("/get/movie/<int:id>", methods=['GET', 'POST'])
    def get_movie(id):
        return(db.get_movie(id))

    @app.route('/post/director', methods=['GET', 'POST'])
    def dir_post(): #adds only at the end of previous objects
        name_give = input('Name of the new director?\n')
        birthday_give = input('Birthday of the new director?\n')
        return(db.post_director(name_give, birthday_give))

    @app.route('/post/actor', methods=['GET', 'POST'])
    def act_post(): #adds only at the end of previous objects
        name_give = input('Name of the new actor?\n')
        birthday_give = input('Birthday of the new actor?\n')
        return(db.post_actor(name_give, birthday_give))

    @app.route('/post/movie' , methods=['GET', 'POST'])
    def movie_post():
        name_give = input('Name of the new movie?\n')
        year = input('Year of the new movie?\n')
        director_id = input('ID of director of the new movie?\n')
        actor_list = list()
        flag = False
        while flag == False:
            actor_id = input('Actor of the new movie?(for exitting press END)\n')
            if actor_id == "END":
                flag=True
            else:
                actor_list.append(actor_id)
        return(db.post_movie(name_give, year, director_id, actor_list))

    @app.route("/update/director/<int:idtk>/" , methods=['GET', 'POST' , 'PUT' , 'PATCH' , 'DELETE' ,'HEAD' , 'OPTIONS'])
    def editDir(idtk):
        name_give = input('New name?\n')
        birthday_give = input('New birthday?\n')
        return(db.put_director(idtk, name_give, birthday_give))

    @app.route("/update/actor/<int:idtk>/" , methods=['GET', 'POST' , 'PUT' , 'PATCH' , 'DELETE' ,'HEAD' , 'OPTIONS'])
    def editAct(idtk):
        name_give = input('New name?\n')
        birthday_give = input('New birthday?\n')
        return(db.put_actor(idtk, name_give, birthday_give))

    @app.route("/update/movie/<int:idtk>/" , methods=['GET', 'POST' , 'PUT' , 'PATCH' , 'DELETE' ,'HEAD' , 'OPTIONS'])
    def editMov(idtk):
        name_give = input('New movie name?\n')
        year = input('New movie year?\n')
        director_id = input('New movie director ID?\n')
        actor_list = list()
        flag = False
        while flag == False:
            actor_id = input('New movie actor?(for exitting press END)\n')
            if actor_id == "END":
                flag=True
            else:
                actor_list.append(actor_id)
        return(db.put_movie(idtk, name_give, year, director_id, actor_list))

    @app.route("/delete/director/<int:idtk>" , methods=['GET', 'POST' , 'PUT' , 'DELETE'])
    def del_director(idtk):
        return(db.delete_director(idtk))

    @app.route("/delete/actor/<int:idtk>" , methods=['GET', 'POST' , 'PUT' , 'DELETE'])
    def del_actor(idtk):
        return(db.delete_actor(idtk))

    @app.route("/delete/movie/<int:idtk>" , methods=['GET', 'POST' , 'PUT' , 'DELETE'])
    def del_movie(idtk):
        return(db.delete_movie(idtk))

app.run(debug=True)