# write me a program that works with a sql database sqlite3 
# and a table with the following fields:
# id, name, age, email, phone
# the program should be able to:
# 1. add a new record
# 2. update a record
# 3. delete a record
# 4. list all records
# 5. search for a record by name
# 6. search for a record by email
# 7. search for a record by phone
# 8. search for a record by age
# 9. search for a record by id
# 10. exit the program
# the program should be able to handle errors and exceptions
# the program should have a menu to select the options
# the program should have a function to create the table if it doesn't exist
# the program should have a function to drop the table
# the program should have a function to connect to the database
# the program should have a function to disconnect from the database
# the program should have a function to add a record
# the program should have a function to update a record
# the program should have a function to delete a record
# the program should have a function to list all records
# the program should have a function to search for a record by name
# the program should have a function to search for a record by email
# the program should have a function to search for a record by phone
# the program should have a function to search for a record by age
# the program should have a function to search for a record by id
# the program should have a function to exit the program
# the program should have a function to handle errors and exceptions
# the program should have a function to display the menu
# the program should have a function to handle the menu options
# the program should have a function to handle the user input
# the program should have a function to validate the user input
# the program should have a function to display the records
# the program should have a function to get the records
# the program should have a function to get the record
# the program should have a function to execute a query 
# the program should have a function to create the table 
# the program should have a function to drop the table
# the program should have a function to connect to the database
# the program should have a function to disconnect from the database
# the program should have a function to add a record
# the program should have a function to update a record
# the program should have a function to delete a record
# the program should have a function to list all records
# the program should have a function to search for a record by name
# the program should have a function to search for a record by email
# the program should have a function to search for a record by phone
# the program should have a function to search for a record by age
# the program should have a function to search for a record by id
# the program should have a function to exit the program
# the program should have a function to handle errors and exceptions
# the program should have a function to display the menu
# the program should have a function to handle the menu options
# the program should have a function to handle the user input
# the program should have a function to validate the user input
# the program should have a function to display the records
# the program should have a function to get the records
# the program should have a function to get the record
# the program should have a function to execute a query
# the program should have a function to create the table
# the program should have a function to drop the table
# the program should have a function to connect to the database
# the program should have a function to disconnect from the database
# the program should have a function to add a record
# the program should have a function to update a record
# the program should have a function to delete a record
# the program should have a function to list all records
# the program should have a function to search for a record by name
# the program should have a function to search for a record by email
# the program should have a function to search for a record by phone
# the program should have a function to search for a record by age
# the program should have a function to search for a record by id 
# the program should have a function to exit the program
# the program should have a function to handle errors and exceptions
# the program should have a function to display the menu
# the program should have a function to handle the menu options
# the program should have a function to handle the user input
# the program should have a function to validate the user input
# the program should have a function to display the records 

import sqlite3 
import os


def create_table():
    try:
        conn = sqlite3.connect('capilot.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS capilot (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(e) 


def drop_table():
    try:
        conn = sqlite3.connect('capilot.db')
        cursor = conn.cursor()
        cursor.execute('''
            DROP TABLE IF EXISTS capilot
        ''')
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


def connect(): 
    try:
        conn = sqlite3.connect('capilot.db')
        return conn
    except Exception as e:
        print(e)



def disconnect(conn):
    try:
        conn.close()
    except Exception as e:
        print(e)

    

def add_record(name, age, email, phone):

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO capilot (name, age, email, phone) VALUES (?, ?, ?, ?)
        ''', (name, age, email, phone))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e) 


def update_record(id, name, age, email, phone):


    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE capilot SET name = ?, age = ?, email = ?, phone = ? WHERE id = ?
        ''', (name, age, email, phone, id))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)



def delete_record(id):


    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM capilot WHERE id = ?
        ''', (id,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


def list_records():


    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM capilot
        ''')
        records = cursor.fetchall()
        conn.close()
        return records
    except Exception as e:
        print(e)


def search_by_name(name):



    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM capilot WHERE name = ?
        ''', (name,))
        records = cursor.fetchall()
        conn.close()
        return records
    except Exception as e:
        print(e)


def search_by_email(email):                         


    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM capilot WHERE email = ?
        ''', (email,))
        records = cursor.fetchall()
        conn.close()
        return records
    except Exception as e:
        print(e)



def search_by_phone(phone):



    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM capilot WHERE phone = ?
        ''', (phone,))
        records = cursor.fetchall()
        conn.close()
        return records
    except Exception as e:
        print(e)



def search_by_age(age):



    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM capilot WHERE age = ?
        ''', (age,))
        records = cursor.fetchall()
        conn.close()
        return records
    except Exception as e:
        print(e)



def search_by_id(id):





    
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM capilot WHERE id = ?
        ''', (id,))
        records = cursor.fetchall()
        conn.close()
        return records
    except Exception as e:
        print(e)




def exit_program():



    os._exit(0)



def handle_errors_and_exceptions(e):


    
        print(e)



def display_menu():

    print('''
        1. Add a new record
        2. Update a record
        3. Delete a record
        4. List all records
        5. Search for a record by name
        6. Search for a record by email
        7. Search for a record by phone
        8. Search for a record by age
        9. Search for a record by id
        10. Exit the program
    ''')


def handle_menu_options(option):
    
        if option == 1:
            name = input('Enter the name: ')
            age = int(input('Enter the age: '))
            email = input('Enter the email: ')
            phone = input('Enter the phone: ')
            add_record(name, age, email, phone)
        elif option == 2:
            id = int(input('Enter the id: '))
            name = input('Enter the name: ')
            age = int(input('Enter the age: '))
            email = input('Enter the email: ')
            phone = input('Enter the phone: ')
            update_record(id, name, age, email, phone)
        elif option == 3:
            id = int(input('Enter the id: '))
            delete_record(id)
        elif option == 4:
            records = list_records()
            display_records(records)
        elif option == 5:
            name = input('Enter the name: ')
            records = search_by_name(name)
            display_records(records)
        elif option == 6:
            email = input('Enter the email: ')
            records = search_by_email(email)
            display_records(records)
        elif option == 7:
            phone = input('Enter the phone: ')
            records = search_by_phone(phone)
            display_records(records)
        elif option == 8:
            age = int(input('Enter the age: '))
            records = search_by_age(age)
            display_records(records)
        elif option == 9:
            id = int(input('Enter the id: '))
            records = search_by_id(id)
            display_records(records)
        elif option == 10:
            exit_program()
        else:
            print('Invalid option')
    

def handle_user_input():
    
        try:
            option = int(input('Enter an option: '))
            handle_menu_options(option)
        except Exception as e:
            handle_errors_and_exceptions(e)
            handle_user_input()



def validate_user_input():
        
            try:
                display_menu()
                handle_user_input()
            except Exception as e:
                handle_errors_and_exceptions(e)
                validate_user_input()


def display_records(records):
    for record in records:
        print(record)


def main():


    create_table()
    validate_user_input()


main()

