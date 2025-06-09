import mysql.connector
from mysql.connector import Error
import os

def execute_sql_script():
    try:
        # Database connection configuration
        connection = mysql.connector.connect(
            host='companysqll.mysql.database.azure.com',
            user='CompanyServers',  
            password='Test@123',    
            database='companydb',
            port=3306,
            ssl_ca='DigiCertGlobalRootCA.crt.pem'
        )

        if connection.is_connected():
            print("Successfully connected to MySQL database!")
            cursor = connection.cursor()
            
            # Read and execute the SQL script
            with open('create_projects_table.sql', 'r') as sql_file:
                sql_commands = sql_file.read().split(';')
                
                for command in sql_commands:
                    if command.strip():
                        try:
                            cursor.execute(command)
                            print(f"Successfully executed: {command.strip()}")
                        except Error as e:
                            print(f"Error executing command: {command.strip()}")
                            print(f"Error: {e}")
                
                # Commit the changes
                connection.commit()
                print("All changes committed successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    execute_sql_script() 