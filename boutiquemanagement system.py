import mysql.connector
conn=mysql.connector.connect(
    user='root',
    host='localhost',
    password='',
    database='BoutiqueManagementSystem'
)
cursor=conn.cursor()
#creating customer table
# varr= "create table customers(cust_id int auto_increment,cust_name varchar(255),email varchar(255),password varchar(50),contact varchar(10),address varchar(40),PRIMARY KEY (cust_id))"
# query = "insert into customers(cust_name,email,password,contact,address)values(%s,%s,%s,%s,%s)"
# cust_name=input("enter the name of customer : ")
# email=input("enter the email")
# password=input("kindly enter your password : ")
# contact=input('please enter your contact details : ')
# address=input("please enter your address : ")
# results=(cust_name,email,password,contact,address)
# cursor.execute(query,results)
#creating employees table
# query = "INSERT INTO employees (emp_name, role, password) VALUES (%s,%s,%s)"
# emp_name=input("enter your name : ")
# role=input('enter your role : ')
# password=input("enter your password : ")
# result=(emp_name,role,password)
# cursor.execute(query,result)
# conn.commit()



# #creating product table
# varrrr="create table products(product_id int auto_increment,product_name varchar(255),price decimal(10,5),stock int, PRIMARY KEY (product_id) )"
# query = "INSERT INTO products (product_name,price, stock) VALUES (%s,%s,%s)"
# product_name=input("enter the product name")
# price=input("enter the actual price of product : ")
# stock=input('enter the stock available')
# result=(product_name,price,stock)
# cursor.execute(query,result)

# #creating order table
# var="create table orders(order_id int auto_increment,customer_id int,product_id int,quantity int,status varchar(20),PRIMARY KEY(order_id),FOREIGN KEY (customer_id)REFERENCES customers(cust_id),FOREIGN KEY (product_id) REFERENCES products(product_id))"
# query = "INSERT INTO orders (customer_id, product_id, quantity, status) VALUES (%s,%s,%s,%s)"
# cust_id=input("enter the customer id : ")
# product_id=input("enter the product id : ")
# quantity=input("enter the quantity : ")
# status=input("enter the order status of product : ")
# result=(cust_id,product_id,quantity,status)
# cursor.execute(query,result)
query = "UPDATE orders SET status='Delivered' WHERE order_id=1"
cursor.execute(query)
# conn.commit()

# cursor.execute(var)
conn.commit()
