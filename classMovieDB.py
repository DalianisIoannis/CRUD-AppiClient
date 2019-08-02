import json
import requests
import urllib3

class MovieDB():
    def __init__(self, BaseURL, username, password, proxie1s):
        self.BaseURL = BaseURL
        self.proxie1s = proxie1s
        self.data = "username="+username+"&password="+password
        temp1 = ((requests.post(BaseURL+"api/api-token-auth/", data=self.data, verify=False , proxies=self.proxie1s, headers={'Content-Type': "application/x-www-form-urlencoded"})).text)
        temp2 = json.loads(temp1)
        self.myToken = "Token" + " " + temp2['token']
        self.headers = {}
        # self.headers['Content-Type'] = "application/json" #unecessary if in requests i have json=data
        self.headers['Authorization'] = self.myToken
        print(self.headers)
    
    def AppiClient(self, request_type, url, data=None):
        try:
            response = requests.request(request_type, url, json=data, verify=False, proxies=self.proxie1s, headers=self.headers)
            return(response)
        except:
            print("Request can't be made.")
            return None

    def print_whole_category(self, table):
        URL = self.BaseURL + 'api/' + table
        string_print = ((self.AppiClient("GET", URL)).text).replace('},','\n')
        string_print = string_print.replace('\n' , '}\n')
        string_print = string_print.replace('[' , '')
        string_print = string_print.replace(']' , '')
        print(string_print)

    def get_all(self):
        print("Directors:")
        self.print_whole_category('directors')
        print("Actors:")
        self.print_whole_category('actors')
        print("Movies:")
        self.print_whole_category('movies')

    def get_director(self, id):
        URL = self.BaseURL + 'api/directors/' + str(id)
        print((self.AppiClient("GET", URL)).text)
    
    def get_actor(self, id):
        URL = self.BaseURL + 'api/actors/' + str(id)
        print((self.AppiClient("GET", URL)).text)
    
    def get_movie(self, id):
        URL = self.BaseURL + 'api/movies/' + str(id)
        print((self.AppiClient("GET", URL)).text)

    def post_director(self, name_give, birthday_give):
        payload = {'name' : name_give , 'birthday' : birthday_give}
        URL = self.BaseURL + '/api/directors/'
        print((self.AppiClient("POST", URL, payload)).text)

    def post_actor(self, name_give, birthday_give):
        payload = {'name' : name_give , 'birthday' : birthday_give}
        URL = self.BaseURL + '/api/actors/'
        print((self.AppiClient("POST", URL, payload)).text)

    def post_movie(self, name_give, year, dir_id, act_list=None):
        if self.director_exist(dir_id)==True:
            flag=True
            for i in act_list:
                if self.actor_exist(i)==False:
                    print("Such actor doesn't exist.\n")
                    flag=False
                    break
            if flag==True:
                payload = {'name' : name_give, 'year' : year, 'director' : dir_id, 'actors' : act_list}
                URL = self.BaseURL + '/api/movies/'
                print((self.AppiClient("POST", URL, payload)).text)
        else:
            print("Such director doesn't exist.\n")

    def delete_director(self, id):
        URL = self.BaseURL + '/api/directors/' + str(id)
        print((self.AppiClient("DELETE", URL)).text)

    def delete_actor(self, id):
        URL = self.BaseURL + '/api/actors/' + str(id)
        print((self.AppiClient("DELETE", URL)).text)

    def delete_movie(self, id):
        URL = self.BaseURL + '/api/movies/' + str(id)
        print((self.AppiClient("DELETE", URL)).text)

    def director_exist(self, idtk):
        req = self.AppiClient("GET", self.BaseURL + 'api/directors/' + str(idtk))
        if (req).status_code==200:
            return True
        else:
            return False

    def actor_exist(self, idtk):
        req = self.AppiClient("GET", self.BaseURL + 'api/actors/' + str(idtk))
        if (req).status_code==200:
            return True
        else:
            return False

    def put_director(self , idtk , name_give , birthday_give):
        payload = {"name" : name_give , "birthday" : birthday_give}
        URL = self.BaseURL + '/api/directors/' + str(idtk) + '/'
        print((self.AppiClient("PUT", URL , payload)).text)

    def put_actor(self , idtk , name_give , birthday_give):
        payload = {"name" : name_give , "birthday" : birthday_give}
        URL = self.BaseURL + '/api/actors/' + str(idtk) + '/'
        print((self.AppiClient("PUT", URL , payload)).text)
    
    def put_movie(self , idtk , name_give , year, dir_id, act_list):
        if self.director_exist(dir_id)==True:
            flag=True
            for i in act_list:
                if self.actor_exist(i)==False:
                    print("Such actor doesn't exist.\n")
                    flag=False
                    break
            if flag==True:
                payload = {'name' : name_give, 'year' : year, 'director' : dir_id, 'actors' : act_list}
                URL = self.BaseURL + '/api/movies/' + str(idtk) + '/'
                print((self.AppiClient("PUT", URL , payload)).text)
        else:
            print("Such director doesn't exist.\n")

    def patch_director(self, idtk, name_give):
        payload = {"name" : name_give}
        URL = self.BaseURL + '/api/directors/' + str(idtk) + '/'
        print((self.AppiClient("PATCH", URL , payload)).text)

    def patch_actor(self, idtk, name_give):
        payload = {"name" : name_give}
        URL = self.BaseURL + '/api/actors/' + str(idtk) + '/'
        print((self.AppiClient("PATCH", URL , payload)).text)

    def patch_movie(self, idtk, name_give):
        payload = {"name" : name_give}
        URL = self.BaseURL + '/api/movies/' + str(idtk) + '/'
        print((self.AppiClient("PATCH", URL , payload)).text)
