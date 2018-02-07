#!/usr/bin/python
import MySQLdb

 
db = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")   # name of the database
 
# Create a Cursor object to execute queries.
curr = db.cursor()

'''curr.execute( "CREATE TABLE IF NOT EXISTS Restaurant ( restaurant_id int NOT NULL AUTO_INCREMENT, name varchar(45), street varchar(45), city varchar(45), state varchar(45), PRIMARY KEY (restaurant_id))" )

curr.execute( "CREATE TABLE IF NOT EXISTS Menu ( menu_id int NOT NULL AUTO_INCREMENT, restaurant_id int, category varchar(45), FORIENGE KEY(restaurant_id) references Restaurant(restaurant_id),  PRIMARY KEY (menu_id))" )

curr.execute( "CREATE TABLE IF NOT EXISTS MenuItems ( menu_id int NOT NULL, category varchar(45), item_name varchar(45), cuisine varchar(45), FORIENGE KEY(menu_id) references Menu(menu_id))" )
  
'''


TABLES = {}
TABLES['Restaurant'] = (
    "CREATE TABLE IF NOT EXISTS `Restaurant` ("
    "  `restaurant_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(20) ,"
    "  `street` varchar(20) ,"
    "  `city` varchar(20) ,"
    "  `state` varchar(20) ,"
    "  PRIMARY KEY (`restaurant_id`)"
    ")")

TABLES['Menu'] = (
    "CREATE TABLE IF NOT EXISTS `Menu` ("
    "  `menu_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `restaurant_id` int(11) ,"
    "  `category` varchar(20) ,"
    "  PRIMARY KEY (`menu_id`)"
#    "  FORIENGE KEY(`restaurant_id`) references Restaurant(`restaurant_id`) ,"
    ") ")

TABLES['MenuItems'] = (
    "CREATE TABLE IF NOT EXISTS `MenuItems` ("
    "  `menu_id` int(11) NOT NULL,"
    "  `category` varchar(20) ,"
    "  `item_name` varchar(20) ,"
    "  `cuisine` varchar(20)"
#    "  FORIENGE KEY(`menu_id`) references Menu(`menu_id`) ,"
    ")")


TABLES['OrderItem'] = (
    "CREATE TABLE IF NOT EXISTS `OrderItem` ("
    "  `order_id` int(11) NOT NULL,"
    "  `item_name` varchar(20) "
#    "  FORIENGE KEY(`menu_id`) references Menu(`menu_id`) ,"
    ")")



for name, ddl in TABLES.iteritems():
    #print("Creating table {}: ".format(name), end='')
    curr.execute(ddl)



curr.execute (" INSERT INTO Restaurant VALUES (%s, %s,%s, %s,%s) ", (1, "Kailash", "HealthScience25", "Stony Brook", "New York"))
curr.execute (" INSERT INTO Restaurant VALUES (%s, %s,%s, %s,%s) ", (2, "CurryClub", "HealthScience25", "Stony Brook", "New York"))
curr.execute (" INSERT INTO Restaurant VALUES (%s, %s,%s, %s,%s) ", (3, "Panera", "HealthScience25", "Stony Brook", "New York"))
curr.execute (" INSERT INTO Restaurant VALUES (%s, %s,%s, %s,%s) ", (4, "Sweet", "HealthScience25", "Stony Brook", "New York"))


curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (1, 1, "Breakfast"))
curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (2, 1, "Lunch"))
curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (3, 1, "Dinner"))
curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (4, 2, "Breakfast"))
curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (5, 2, "Lunch"))
curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (6, 2, "Dinner"))
curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (7, 3, "Breakfast"))
curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (8, 3, "Lunch"))
curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (9, 3, "Dinner"))
curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (10, 4, "Breakfast"))
curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (11, 4, "Lunch"))
curr.execute (" INSERT INTO Menu VALUES (%s, %s,%s) ", (12, 4, "Dinner"))



curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (1, "Breakfast", "Idli", "Indian"))
curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (1, "Breakfast", "Poha", "Indian"))
curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (2, "Lunch", "Chicken", "Italian"))
curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (4, "Breakfast", "Bread", "American"))
curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (5, "Lunch", "Turkey", "Mexican"))
curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (5, "Lunch", "Becon", "American"))
curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (6, "Lunch", "Chicken", "Italian"))
curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (6, "Dinner", "Roti", "Indian"))
curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (9, "Dinner", "Pizza", "American"))
curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (9, "Dinner", "Paneer", "Indian"))
curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (9, "Dinner", "ChickenCurry", "American"))
curr.execute (" INSERT INTO MenuItems VALUES (%s, %s,%s, %s) ", (12, "Dinner", "BreadJam", "American"))


curr.execute("SELECT * FROM Restaurant")
for row in curr.fetchall() :
    print row[0], " ", row[1], " ", row[2], " ", row[3], " ", row[4]
    
curr.execute("SELECT * FROM Menu")
for row in curr.fetchall() :
	print row[0], " ", row[1], " ", row[2]


curr.execute("SELECT * FROM MenuItems")
for row in curr.fetchall() :
    print row[0], " ", row[1], " ", row[2], " ", row[3]

db.commit() 
curr.close()



