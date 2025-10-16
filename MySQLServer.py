import mysql.connector
from mysql.connector import Error

def Create_DB():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
        if mydb.is_connected():
            cursor = mydb.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print(" Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as e:
        print(f"An Error Occured {e}")
    finally:
        if mydb and mydb.is_connected():
            cursor.close()
            mydb.close()
            print("MySQL connection is closed")


if __name__ == "__main__":
    Create_DB()


