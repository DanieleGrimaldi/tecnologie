import mysql.connector
from mysql.connector import Error
import pandas as pd

class Connessione:
    def __init__(self, host_name, user_name, user_password, db_name):
        self.connection =  mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print(self.connection.get_server_info())
        self.cursor =self.connection.cursor()


    def execute_query(self,query):
    
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    def execute_multiquery(self,query):
    
        try:
            self.cursor.execute(query, multi=True)
            self.connection.commit()
        except Error as err:
            print(f"Error: '{err}'") 


    def read_query(self, query):
        
        result = None
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchmany()
            return result
        except Error as err:
            print(f"Error: '{err}'")