from flask import Flask

import pymysql

app = Flask(__name__)

# def db_connection():
#     connection = pymysql.connect(
#         host='db',
#         user='user',
#         password='password',
#         database='mydatabase'
#     )
#     return connection

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/insert_data')
def insert_data():
    # Connection to the database
    connection = pymysql.connect(
        host='mysql_container',  # why my_sql_container? and not local host?
        user='root',
        password='demopassword',
        database='demodb'
    )
    
    # Create a cursor object    
    cursor = connection.cursor()
    
    # Insert data into the table
    insert_query = "INSERT INTO users (city, temperature) VALUES (%s, %s)"
    
    data = ('New York', 25)
    
    cursor.execute(insert_query, data)
    
    #Commit the transaction
    connection.commit()
    
    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    return "Data inserted successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
    
    