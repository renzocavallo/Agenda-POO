from tkinter import ttk

class Treeview():
    def __init__(self, root):
    
        style = ttk.Style()
        style.theme_use("clam")
    
        self.treeview = ttk.Treeview(root)
        self.treeview["columns"] = ("col1", "col2", "col3", "col4", "col5")
        self.treeview.column("#0", width=0, minwidth=0)
        self.treeview.column("col1", width=60, minwidth=60)
        self.treeview.heading("col1", text="Id")
        self.treeview.column("col2", width=60, minwidth=60)
        self.treeview.heading("col2", text="Nombre")
        self.treeview.column("col3", width=80, minwidth=60)
        self.treeview.heading("col3", text="Apellido")
        self.treeview.column("col4", width=130, minwidth=80)
        self.treeview.heading("col4", text="Telefono")
        self.treeview.column("col5",width=130, minwidth=80)
        self.treeview.heading("col5", text="Email")
        self.treeview.place(x= 20, y=0)
    
    def get_treeview(self):
        return self.treeview