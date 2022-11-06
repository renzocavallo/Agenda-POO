from tkinter import ttk
from tkinter import END
from src.components.button import Bton
from src.components.bton_properties import bton_c
from src.components.bton_properties import bton_search
from src.components.label_entry import Label_entry
from src.components.label_entry_properties import label_search
from config.model_controller import get_all_contacts
from config.model_controller import get_contact_by_name
from util.view import refresh_insert_treeview

class Seeker_contacts():
    def __init__(self, root, treeview):
        self.seeker_c = ttk.LabelFrame(root)
        self.seeker_c.place(y=170, width= 500, height=65)

        def click_contacts():
           contacts = get_all_contacts()
           refresh_insert_treeview(treeview, contacts)

        Bton(self.seeker_c, bton_c, click_contacts)

        label_entry_query = Label_entry(self.seeker_c, label_search)
        entry_query = label_entry_query.get_entry()

        def click_search():
            contacts_search = get_contact_by_name(entry_query.get())
            refresh_insert_treeview(treeview, contacts_search)
            entry_query.delete(0, END)   

        Bton(self.seeker_c, bton_search, click_search)