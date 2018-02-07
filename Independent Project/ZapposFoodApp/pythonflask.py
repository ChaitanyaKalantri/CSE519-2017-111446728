from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
import MySQLdb


app = Flask(__name__)
api = Api(app)


# get function complete:
class Restaurant(Resource):
    def get(self):
        #conn = db_connect.connect() # connect to database
        db_connect = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
        conn = db_connect.cursor()
        query = conn.execute("select * from Restaurant") # This line performs query and returns json result
        return {'Restaurant': [i[0] for i in conn.fetchall()]} # Fetches first column that is Employee ID

    def post(self):
        db_connect = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
        conn = db_connect.cursor()
        print(request.json)
        RestaurantId = request.json['restaurant_id']
        Name = request.json['name']
        Street = request.json['street']
        City = request.json['city']
        State = request.json['state']
        
        query = conn.execute("insert into Restaurant values(null,'{0}','{1}','{2}','{3}', '{4}' )".format(RestaurantId,Name,Stree, City, State))
        return {'status':'success'}



class Menu(Resource):
    def get(self):
        #conn = db_connect.connect() # connect to database
        db_connect = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
        conn = db_connect.cursor()
        query = conn.execute("select * from Menu") # This line performs query and returns json result
        return {'Menu': [i[0] for i in conn.fetchall()]} # Fetches first column that is Employee ID

    def post(self):
        db_connect = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
        conn = db_connect.cursor()
        print(request.json)
        MenuId = request.json['menu_id']
        RestaurantId = request.json['restaurant_id']
        Category = request.json['category']
        
        query = conn.execute("insert into Menu values(null,'{0}','{1}','{2}' )".format(MenuId,RestaurantId,Category))
        return {'status':'success'}



class MenuItems(Resource):
    def get(self):
        #conn = db_connect.connect() # connect to database
        db_connect = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
        conn = db_connect.cursor()
        query = conn.execute("select * from MenuItems") # This line performs query and returns json result
        return {'MenuItems': [i[0] for i in conn.fetchall()]} # Fetches first column that is Employee ID

    def post(self):
        db_connect = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
        conn = db_connect.cursor()
        print(request.json)
        MenuId = request.json['menu_id']
        Category = request.json['category']
        ItemName = request.json['item_name']
        
        query = conn.execute("insert into employees values(null,'{0}','{1}','{2}' )".format(MenuId,Category,ItemName))
        return {'status':'success'}

        

api.add_resource(Restaurant, '/Restaurant') # Route_1
api.add_resource(Menu, '/Menu') # Route_1
api.add_resource(MenuItems, '/MenuItems') # Route_1



if __name__ == '__main__':
     app.run(port='5002')
     