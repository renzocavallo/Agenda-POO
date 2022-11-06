from tkinter import *
from tkinter import ttk

def insert_treeview(treeview:ttk.Treeview, contacts:list):

     treeview.insert(
          "", 
          "end", 
          values= (
               contacts[len(contacts)-1][0], 
               contacts[len(contacts)-1][1], 
               contacts[len(contacts)-1][2], 
               contacts[len(contacts)-1][3],
               contacts[len(contacts)-1][4]
          )
     )

def refresh_insert_treeview(treeview:ttk.Treeview, contacts:list):

     for item in treeview.get_children():
          
        treeview.delete(item)

     for i in range(len(contacts)):

        treeview.insert(
          "", 
          "end",
          values= (
               contacts[i][0], 
               contacts[i][1], 
               contacts[i][2], 
               contacts[i][3], 
               contacts[i][4]
          )
     )

def refresh_entrys(name:Entry, lastname:Entry, phone:Entry, email:Entry):

     name.delete(0, END)
     lastname.delete(0, END)
     phone.delete(0, END)
     email.delete(0, END)
     name.focus_set()

def insert_entrys_item(
     entry_name:Entry, 
     entry_lastname:Entry, 
     entry_phone:Entry, 
     entry_email:Entry, 
     treeview:ttk.Treeview, 
     item):
     
     entry_name.insert(0, treeview.item(item)["values"][1])
     entry_lastname.insert(0, treeview.item(item)["values"][2])
     entry_phone.insert(0, treeview.item(item)["values"][3])
     entry_email.insert(0, treeview.item(item)["values"][4])