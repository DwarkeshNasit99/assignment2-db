import mysql.connector
from mysql.connector import Error
import os

def execute_sql_script():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='', 
            database='companydb'  
        )

        if connection.is_connected():
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