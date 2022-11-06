import re

def name_patron(name):
    
    patron = re.compile("^[A-Z]+[a-záéíóú]+$")

    return patron.match(name)

def lastname_patron(lastname): 
    
    patron = re.compile("^[A-Z]+[a-záéíóú]+$")

    return patron.match(lastname)

def phone_patron(phone):
    
    patron = re.compile("(^[+]+([0-9]{1,3}))+([-]+([0-9]{1,4}))+[-]+[0-9]+$")

    return patron.match(phone)

def email_patron(email):
    
    patron = re.compile("^$|^[a-z0-9_]+[@]+(gmail|hotmail|hubspot|protonmail|icloud)+(.com)+$")
    
    return patron.match(email)