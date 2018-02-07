from flask import Flask, render_template, request
import MySQLdb


app = Flask(__name__)

orderid = 0

@app.route("/")
def Restaurant():
	db_connect = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
	conn = db_connect.cursor()
	query = conn.execute("select * from Restaurant") # This line performs query and returns json result
	result = {'Restaurant': [i[1] for i in conn.fetchall()]} # Fetches first column that is Employee ID
	#print(result)
	return render_template("index.html", result = result)

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


@app.route("/", methods=['GET', 'POST'])
def MenuItems():
	print("Menu Items")
	db_connect = MySQLdb.connect(host="localhost", user="root",  db="pythonspot")
	conn = db_connect.cursor()
	rest = request.form['r']
	print(rest)
	query = conn.execute("select * from MenuItems where menu_id =  " ) 

	result = {'MenuItems': [i[2] for i in conn.fetchall()]} # Fetches first column that is Employee ID
	print(result)
	return render_template("menuItems.html", result = result)

if __name__ == "__main__":
	app.run(port=5002)







