from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

#Declared global orderid; as I am assuming that once the application is running online it won't stop in between
orderid = 0

# This method will display all the names of the restaurant to the user
# The python flask logic will take the help of index.html page to display the restaurant names
@app.route("/")
def Restaurant():
	db_connect = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
	conn = db_connect.cursor()
	query = conn.execute("select * from Restaurant") # This line performs query and returns json result
	result = {'Restaurant': [i[1] for i in conn.fetchall()]} # Fetches first column that is Employee ID
	#print(result)
	return render_template("index.html", result = result)

# This method will first check if the return value is item; that means it has the list of all the items and hence this will have its own logic
# The python flask logic will take the help of success.html page to display the item names selected
# In the elif part; we will check if the return valu is order; then we will display the showOrder.html page, rest all is self explanatory
# And finally in else logic, we have two parts:
# Based on the return type of the return type, which I am storing it in variable "rest"; if the type of rest is int, then try logic will be executed
# and the menuItems.html page will be called
# Otherwise, the except ValueError will be executed and this will execute the menu.html page
# Rest the logic part of all the functions is just to get the revelant values from the respective tables stored in the mysql database and display them using html pages

@app.route("/", methods=['GET','POST'])
def Menu():
	global orderid
	db_connect = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
	conn = db_connect.cursor()

	if request.form.get('item'):
		result = request.form.getlist('item')
		#query = conn.execute("select max(order_id) from OrderItem")
		#print(query)
		orderid = orderid + 1

		print(orderid) 
		for item in result:
			conn.execute (" INSERT INTO OrderItem VALUES (%s, %s) ", (orderid, item ))
		db_connect.commit() 
		
		return render_template("success.html", result=orderid )
	elif request.form.get('order'):
		orderID = request.form['order']
		#query = conn.execute("select max(order_id) from OrderItem")
		#print(query)
		print("Order Items")
		query = conn.execute("select * from OrderItem where order_id = %d " % int(orderID) ) 
		result = {'OrderItems': [i[1] for i in conn.fetchall()]}
		return render_template("showOrder.html", result=result )
	else:
		rest = request.form['r']
		rest = rest.strip()
		print(rest)
		print(request.method)
		try:
			print("Menu Items")
			query = conn.execute("select * from MenuItems where menu_id = %d " % int(rest) ) 
			result = {'MenuItems': [i[2] for i in conn.fetchall()]} # Fetches first column that is Employee ID
			#print(result)
			return render_template("menuItems.html", result = result)
		except ValueError:
			print("Menu")
			sql_string = "select * from Menu where restaurant_id = ( select restaurant_id from Restaurant where name = '%s' )"
			query = conn.execute( sql_string % rest)

			result = {'Menu': [(int(i[0]), i[2]) for i in conn.fetchall()]} # Fetches first column that is Employee ID
			#print(result)
			return render_template("menu.html", result = result)

# The application will run on port number 5002
if __name__ == "__main__":
	app.run(port=5002)
