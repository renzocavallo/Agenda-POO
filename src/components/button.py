from tkinter import Button

class Bton():
    def __init__(self, root, bton_propertys, function):
        bton = Button(
        root, 
        text = bton_propertys["text"],
        bg = bton_propertys["bg"], 
        fg = bton_propertys["fg"], 
        activebackground = bton_propertys["active_bg"], 
        activeforeground = bton_propertys["active_fg"],
        command = function
        )

        bton.place(x = bton_propertys["place_x"], y = bton_propertys["place_y"])
