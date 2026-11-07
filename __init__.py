import tkinter
from tkinter import *
# from random import *
# from smtplib import SMTP_SSL
# from yagmail import SMTP
from tkinter import scrolledtext, ttk



class Branding_Text(Label):
    def __init__(self, win,bg_color, branding_text, fg_color, text_size: int, xy_cor: tuple):
        super().__init__(win,background=bg_color, text=branding_text, foreground=fg_color, font=("Fixedsys", text_size))
        self.place(x=xy_cor[0], y=xy_cor[1])


#UDN- Tkinter Module
class DynamicPanel(Canvas):
    def __init__(self, win, panel_size:tuple, xy_cor:tuple, panel_bgcolor:str, panel_border_color:str):
        super().__init__(win, width=panel_size[0], height=panel_size[1], highlightthickness=panel_size[2], bg=panel_bgcolor.lower(),
                         highlightbackground=panel_border_color)
        self.place(x=xy_cor[0], y=xy_cor[1])



class TextLabel(Label):
    def __init__(self, win, bg_color: str, text: str, text_color: str, font_details: tuple, xy_cor: tuple):
        super().__init__(win,background=bg_color, text=text, foreground=text_color, font=font_details)

        self.place(x=xy_cor[0], y=xy_cor[1])

class Panel_Tag(Label):
    def __init__(self, win, panel_name:str, text_size: int, xy_cor: tuple):
        super().__init__(win,background="Black", text=panel_name, foreground="Red", font=("Fixedsys", text_size))
        self.place(x=xy_cor[0], y=xy_cor[1])

class SButton(Button):
    def __init__(self,win, button_size:tuple, button_color:str, text_color:str, active_button_color:str, active_text_color:str, button_name:str, button_text_size:int, button_text:str,
                 xy_cor:tuple, button_action):
        super().__init__(win, width=button_size[0], height=button_size[1],background=button_color, activeforeground=active_text_color, activebackground=active_button_color,
                         foreground=text_color, text=button_name, font=(button_text, button_text_size), command=button_action)

        self.place(x=xy_cor[0], y=xy_cor[1])

class RadioButton(Radiobutton):
    def __init__(self, win, button_name, xy_cor, bg_color, textcolor, button_width, button_action, text_size, value, variable):
        super().__init__(win, text=button_name.title(), bg=bg_color, value=value, variable=variable, fg=textcolor, width=button_width, command=action, font=("Georgia", text_size), highlightthickness=0, activebackground=bg_color, disabledforeground="black")
        self.place(x=xy_cor[0], y=xy_cor[1])

class TextEntry(Entry):
    def __init__(self, win, entry_width: int, entry_text:str, entry_text_size:tuple, xy_cor:tuple):
        super().__init__(win, font=("Helvetica", entry_text_size), width=entry_width)
        self.insert(0, entry_text)
        self.place(x=xy_cor[0], y=xy_cor[1])

    def delete_text(self):
        self.delete(0, tk.END)

    def text(self, text_value):
        self.insert(0, text_value)


class LongEntry(Text):
    def __init__(self, win, xy_cor: tuple, entry_box_size:tuple, entry_text_size:int):
        super().__init__(win, font=("Helvetica", entry_text_size), width=entry_box_size[0], height=entry_box_size[1])
        self.place(x=xy_cor[0], y=xy_cor[1])

    def text(self, entry_text):
        self.insert(tkinter.END, entry_text)
class ScrollEntry(scrolledtext.ScrolledText):
    def __init__(self, win, xy_cor: tuple, entry_box_size:tuple, entry_text_size:int):
        super().__init__(win, font=("Helvetica", entry_text_size), width=entry_box_size[0], height=entry_box_size[1])
        self.place(x=xy_cor[0], y=xy_cor[1])


class DropDown(ttk.Combobox):
    def __init__(self, win, select_action, items: list, xy_cor: tuple, box_size, text_size, variable,
                 default_text: str = ""):
        super().__init__(
            win,
            values=items,
            width=box_size[0],
            height=box_size[1],
            state="readonly",
            font=("Helvetica", text_size),
            textvariable=variable
        )
        self.place(x=xy_cor[0], y=xy_cor[1])

        # The condition to set the default text
        if default_text != "":
            variable.set(default_text)

class ListBox(Listbox):

    def __init__(self, win, size: tuple, xy_cor: tuple, variable, text_size: int):
        super().__init__(win, width=size[0], height=size[1],font=("Helvetica", text_size),
                         listvariable=variable, yscrollcommand=Scrollbar(win, orient="vertical"), xscrollcommand=Scrollbar(win, orient="horizontal"))
        self.place(x=xy_cor[0], y=xy_cor[1])


    def add_item(self, index, value):
        self.insert(index, value)

    def get_value(self):
        item = self.curselection()
        if item:
            return self.get(item[0])
        else:
            return "None"



class WarVer(Label):
    def __init__(self, bg_color, text_size, text, xy_cor, war_ver):
        super().__init__(bg=bg_color, text=text, font=("Times New Roman", text_size))
        if war_ver == "war":
            self.config(fg=f"#{choice(colors_warning).lower()}")
        elif war_ver == "ver":
            self.config(fg=f"#{choice(colors_verify).lower()}")
        else:
            pass
        self.place(x=xy_cor[0], y=xy_cor[1])

class CheckButton(Checkbutton):
    def __init__(self, win, button_name: str, xy_cor: tuple, bg_color: str, textcolor: str, text_size: int, variable, button_action=None, on_val=1, off_val=0):
        super().__init__(
            win,
            text=button_name.title(),
            bg=bg_color,
            fg=textcolor,
            variable=variable,
            command=button_action,
            font=("Georgia", text_size),
            highlightthickness=0,
            activebackground=bg_color,
            activeforeground=textcolor,
            selectcolor="white",
            onvalue=on_val,   # Sets the value when checked
            offvalue=off_val  # Sets the value when unchecked
        )
        self.place(x=xy_cor[0], y=xy_cor[1])