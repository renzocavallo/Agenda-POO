from tkinter import Tk
from src.conteiners.form import Form
from src.components.button import Bton
from src.conteiners.buttons_pad import Buttons_pad
from src.components.bton_properties import bton_quit
from src.conteiners.view_contact import View_contacts
from src.conteiners.seeker_contacts import Seeker_contacts
from config.model_controller import get_all_contacts

app = Tk()

app.title("Agenda Telefónica")
app.geometry("500x550")

contacts = get_all_contacts()

form = Form(app)

entry_name = form.get_entry_name()
entry_lastname = form.get_entry_lastname()
entry_email = form.get_entry_email()
entry_phone = form.get_entry_phone()

view_contacts = View_contacts(app)
treeview = view_contacts.get_view_treeview()

buttons_pad = Buttons_pad(app, entry_name, entry_lastname, entry_email, entry_phone, treeview)

Seeker_contacts(app, treeview)

for i in range(len(contacts)):
    
    treeview.insert(
        "", 
        "end", 
        values = (contacts[i][0], contacts[i][1], contacts[i][2], contacts[i][3], contacts[i][4])
    )

Bton(app, bton_quit, quit)

app.mainloop()