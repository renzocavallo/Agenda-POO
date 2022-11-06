import sqlite3
from util.validators import *

db_proyect= sqlite3.connect("db_agenda.db")

try:
    
    cursor_db_proyect = db_proyect.cursor()
    query = """ CREATE TABLE contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre  VARCHAR (250) NOT NULL,
                apellido VARCHAR (250) NOT NULL,
                telefono VARCHAR (50) NOT NULL,
                email VARCHAR (250)
    )
    """
    cursor_db_proyect.execute(query)

except:
    
    print("La tabla ya existe")

def get_all_contacts():
    
    query = "SELECT * FROM contacts"
    cursor_db_proyect.execute(query)
    return cursor_db_proyect.fetchall()

def get_contact_by_name(name):
    
    data = (name,)
    query = "SELECT * FROM contacts WHERE nombre = ?;"
    cursor_db_proyect.execute(query, data)
    return cursor_db_proyect.fetchall()

def create_contact(name, lastname, phone, email):
    
    if (name_patron(name) != None 
        and lastname_patron(lastname) != None 
        and phone_patron(phone) != None 
        and email_patron(email) != None):

        data = (name, lastname, phone, email)
        query = "INSERT INTO contacts (nombre, apellido, telefono, email) VALUES(?, ?, ?, ?)"
        cursor_db_proyect.execute(query, data)
        db_proyect.commit()

        return True

    return False    

def delete_contact(id):
    
    data = (id,)
    query = "DELETE FROM contacts WHERE id = ?;"
    cursor_db_proyect.execute(query, data)
    db_proyect.commit()

def edit_contact(name, lastname, phone, email, id):
    
    if (name_patron(name) != None
        and lastname_patron(lastname) != None 
        and phone_patron(phone) != None 
        and email_patron(email) != None):

        data = (name, lastname, phone, email, id)
        query = "UPDATE contacts SET nombre = ?, apellido = ?, telefono = ?, email = ? WHERE id = ?;"
        cursor_db_proyect.execute(query, data)
        db_proyect.commit() 
         
        return True

    return False  