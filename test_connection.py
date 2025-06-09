import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='companysqll.mysql.database.azure.com',
        user='CompanyServers', 
        password='Test@123',    
        database='companydb',
        port=3306,
        ssl_ca='DigiCertGlobalRootCA.crt.pem'
    )
    
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed") 