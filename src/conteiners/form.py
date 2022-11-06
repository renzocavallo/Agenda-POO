from tkinter import ttk
from src.components.label_entry import Label_entry
from src.components.label_entry_properties import *

class Form():

    def __init__(self, root):

        form = ttk.LabelFrame(root, text="DATOS DE CONTACTO :")
        form.place(width=250, height=180)

        label_entry_name = Label_entry(form, label_n)
        self.entry_name = label_entry_name.get_entry()

        label_entry_lastname = Label_entry(form, label_l)
        self.entry_lastname = label_entry_lastname.get_entry()

        label_entry_email = Label_entry(form, label_e)
        self.entry_email = label_entry_email.get_entry()

        label_entry_phone = Label_entry(form, label_p)
        self.entry_phone = label_entry_phone.get_entry()

    def get_entry_name(self):
        return self.entry_name

    def get_entry_lastname(self):
        return self.entry_lastname

    def get_entry_email(self):
        return self.entry_email

    def get_entry_phone(self):
        return self.entry_phone