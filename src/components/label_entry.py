from tkinter import Label
from tkinter import Entry

class Label_entry():
    def __init__(self, root, label_entry_p):
        self.label = Label(root, text = label_entry_p["text"])
        self.label.place(x = label_entry_p["label_x"], y = label_entry_p["label_y"])
        self.entry = Entry(root)
        self.entry.place(x = label_entry_p["entry_x"], y = label_entry_p["entry_y"])

    def get_entry(self):
        return self.entry