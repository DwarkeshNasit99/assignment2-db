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
        cursor = connection.cursor()
        with open('add_departments.sql', 'r') as sql_file:
            sql_commands = sql_file.read().split(';')
            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)
                    print(f'Successfully executed: {command.strip()}')
        connection.commit()
        print('All changes committed successfully!')
except Error as e:
    print(f'Error: {e}')
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed.')