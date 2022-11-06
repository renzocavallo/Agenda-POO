from tkinter import ttk
from tkinter.messagebox import *
from src.components.button import Bton
from src.components.bton_properties import *
from util.view import *
from config.model_controller import *

class Buttons_pad():
    def __init__(self, root, name, lastname, email, phone, treeview):

        buttons = ttk.LabelFrame(root)
        buttons.place(x=250, width=250, height=180)

        def click_bton_save():
            if create_contact(
                name.get(), 
                lastname.get(), 
                phone.get(), 
                email.get()):
            
                contacts = get_all_contacts()
                insert_treeview(treeview, contacts)
                showinfo(
                    "Contacto Creado",
                    "Se agregó : " + contacts[len(contacts)-1][1] + 
                    " " + contacts[len(contacts)-1][2])
                refresh_entrys(name, lastname, phone, email)
        
            else: 
            
                showerror("Error", "Datos ingresados invalidos") 

        Bton(buttons, bton_s, click_bton_save)

        def click_bton_delete():
            if treeview.focus():
                contacts = get_all_contacts()
                item = treeview.focus()
        
                if askyesno(
                    "Eliminar Contacto: ", 
                    "Desea eliminar: " + treeview.item(item)["values"][1] + 
                    " " + treeview.item(item)["values"][2] +"?"):

                    showinfo("Si", "Contacto eliminado")

                    delete_contact(treeview.item(item)["values"][0])
                    count = 0
            
                    for i in range(len(contacts)):
                
                        if contacts[i][0] != treeview.item(item)["values"][0]:
                            count += 1

                        else:
                        
                           break
        
                    contacts.pop(count)
                    treeview.delete(item)

        Bton(buttons, bton_d, click_bton_delete)

        def click_bton_edit():
            if treeview.focus():
            
                item = treeview.focus()
                insert_entrys_item(name, lastname, phone, email, treeview, item)   

        Bton(buttons, bton_e, click_bton_edit)

        def click_bton_confirm():
            if treeview.focus():

                contacts = get_all_contacts()
                item = treeview.focus()
                id = treeview.item(item)["values"][0]
            
                if edit_contact(name.get(), lastname.get(), phone.get(), email.get(), id):

                    if askyesno(
                        "Editar Contacto: ", 
                        "Desea confirmar lo siguiente ? " + 
                        "\n" + name.get() + 
                        "\n" + lastname.get() + 
                        "\n" + phone.get()+
                        "\n" + email.get()):

                        showinfo("Si", "Contacto editado")
                        contacts.clear()
                        contacts = get_all_contacts()
                        refresh_insert_treeview(treeview, contacts)
                        refresh_entrys(name, lastname, phone, email)
        
                    else:

                        showinfo("Editar Contacto", "El contacto no se editó")
                        refresh_entrys(name, lastname, phone, email)
  
            else:
                showerror("Error", "Datos ingresados invalidos")
                refresh_entrys(name, lastname, phone, email) 

        Bton(buttons, bton_confirm_e, click_bton_confirm)