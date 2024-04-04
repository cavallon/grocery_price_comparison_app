import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('grocery.sqlite')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the store table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS store")
 
# Creating table
table = """ CREATE TABLE store (
            id serial,
            store CHAR(255) NOT NULL,
            category CHAR(255),
            PRIMARY KEY (id)
        ); """
 

cursor_obj.execute(table)


# Drop the product table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS product")
cursor_obj.execute("DROP TABLE IF EXISTS products")

table = """CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            product CHAR(255) NOT NULL,
            brand CHAR(255),
            price FLOAT,
            size CHAR(255),
            ingredient CHAR(255),
            store CHAR(255),
            date DATE
        ); """
 
cursor_obj.execute(table)

print("Tables are ready")
 
# Close the connection
connection_obj.close()


