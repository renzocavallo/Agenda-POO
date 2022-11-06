from tkinter import ttk
from src.components.treeview import Treeview

class View_contacts():
    def __init__(self, root):
        self.view_c = ttk.LabelFrame(root, text="AGENDA :")
        self.view_c.place(y= 235, width=500, height=250)

        self.treeview = Treeview(self.view_c)

    def get_view_treeview(self):
        return self.treeview.get_treeview()