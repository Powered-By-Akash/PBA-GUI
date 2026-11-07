"""
PBA-GUI (PBA_GEN2025)
=====================
Modular Python Tkinter GUI Framework & Visual Component Library.
Developed by Powered By Akash (PBA) — Akash Tanna, Gujarat, India.

Core components:
- Branding_Text: Styled fixed-width header and branding text label.
- DynamicPanel: Canvas-backed container panel with border highlighting.
- TextLabel: Generalized styled text label with font styling and coordinates.
- Panel_Tag: High-visibility tag header for engineering consoles.
- SButton: Styled push button with active hover states and callback action.
- RadioButton: Stylized radio button control.
- TextEntry: Single-line entry box with convenience utility methods.
- LongEntry: Multi-line text entry box with append capability.
- ScrollEntry: ScrolledText widget for logs, output streams, and consoles.
- DropDown: Readonly combobox with variable binding and default value selection.
- ListBox: Listbox with vertical/horizontal scroll integration and helper methods.
- WarVer: Warning/Verification alert label with randomized highlight hues.
- CheckButton: Checkbutton toggle with active state color handling.
"""

import tkinter as tk
from tkinter import *
from tkinter import scrolledtext, ttk
import random

# Color palettes for Warning & Verification tags
colors_warning = ["E63946", "FF4D4D", "FF6B6B", "D90429", "EF233C"]
colors_verify = ["2A9D8F", "2EC4B6", "06D6A0", "118AB2", "00B4D8"]


class Branding_Text(Label):
    """Retro fixed-width branding label for headers and titles."""
    def __init__(self, win, bg_color: str, branding_text: str, fg_color: str, text_size: int, xy_cor: tuple):
        super().__init__(win, background=bg_color, text=branding_text, foreground=fg_color, font=("Fixedsys", text_size))
        self.place(x=xy_cor[0], y=xy_cor[1])


class DynamicPanel(Canvas):
    """Canvas-backed container panel with highlight border and coordinate positioning."""
    def __init__(self, win, panel_size: tuple, xy_cor: tuple, panel_bgcolor: str, panel_border_color: str):
        thickness = panel_size[2] if len(panel_size) > 2 else 1
        super().__init__(
            win,
            width=panel_size[0],
            height=panel_size[1],
            highlightthickness=thickness,
            bg=panel_bgcolor.lower(),
            highlightbackground=panel_border_color
        )
        self.place(x=xy_cor[0], y=xy_cor[1])


class TextLabel(Label):
    """General-purpose styled text label with font customization."""
    def __init__(self, win, bg_color: str, text: str, text_color: str, font_details: tuple, xy_cor: tuple):
        super().__init__(win, background=bg_color, text=text, foreground=text_color, font=font_details)
        self.place(x=xy_cor[0], y=xy_cor[1])


class Panel_Tag(Label):
    """High-visibility panel tag for engineering consoles and dashboard panels."""
    def __init__(self, win, panel_name: str, text_size: int, xy_cor: tuple):
        super().__init__(win, background="Black", text=panel_name, foreground="Red", font=("Fixedsys", text_size))
        self.place(x=xy_cor[0], y=xy_cor[1])


class SButton(Button):
    """Styled push button with active hover states and callback action."""
    def __init__(self, win, button_size: tuple, button_color: str, text_color: str, active_button_color: str,
                 active_text_color: str, button_name: str, button_text_size: int, button_text: str,
                 xy_cor: tuple, button_action):
        super().__init__(
            win,
            width=button_size[0],
            height=button_size[1],
            background=button_color,
            activeforeground=active_text_color,
            activebackground=active_button_color,
            foreground=text_color,
            text=button_name,
            font=(button_text, button_text_size),
            command=button_action
        )
        self.place(x=xy_cor[0], y=xy_cor[1])


class RadioButton(Radiobutton):
    """Styled radio button selection control."""
    def __init__(self, win, button_name: str, xy_cor: tuple, bg_color: str, textcolor: str,
                 button_width: int, button_action, text_size: int, value, variable):
        super().__init__(
            win,
            text=button_name.title(),
            bg=bg_color,
            value=value,
            variable=variable,
            fg=textcolor,
            width=button_width,
            command=button_action,
            font=("Georgia", text_size),
            highlightthickness=0,
            activebackground=bg_color,
            disabledforeground="black"
        )
        self.place(x=xy_cor[0], y=xy_cor[1])


class TextEntry(Entry):
    """Single-line entry widget with helper utilities."""
    def __init__(self, win, entry_width: int, entry_text: str, entry_text_size, xy_cor: tuple):
        font_spec = ("Helvetica", entry_text_size) if isinstance(entry_text_size, int) else ("Helvetica", entry_text_size[0])
        super().__init__(win, font=font_spec, width=entry_width)
        if entry_text:
            self.insert(0, entry_text)
        self.place(x=xy_cor[0], y=xy_cor[1])

    def delete_text(self):
        self.delete(0, tk.END)

    def text(self, text_value: str):
        self.insert(0, text_value)


class LongEntry(Text):
    """Multi-line text editor widget."""
    def __init__(self, win, xy_cor: tuple, entry_box_size: tuple, entry_text_size: int):
        super().__init__(win, font=("Helvetica", entry_text_size), width=entry_box_size[0], height=entry_box_size[1])
        self.place(x=xy_cor[0], y=xy_cor[1])

    def text(self, entry_text: str):
        self.insert(tk.END, entry_text)


class ScrollEntry(scrolledtext.ScrolledText):
    """Scrollable text console for streaming logs and outputs."""
    def __init__(self, win, xy_cor: tuple, entry_box_size: tuple, entry_text_size: int):
        super().__init__(win, font=("Helvetica", entry_text_size), width=entry_box_size[0], height=entry_box_size[1])
        self.place(x=xy_cor[0], y=xy_cor[1])


class DropDown(ttk.Combobox):
    """Readonly combobox dropdown with auto-binding and default selection."""
    def __init__(self, win, select_action, items: list, xy_cor: tuple, box_size: tuple, text_size: int,
                 variable, default_text: str = ""):
        super().__init__(
            win,
            values=items,
            width=box_size[0],
            height=box_size[1],
            state="readonly",
            font=("Helvetica", text_size),
            textvariable=variable
        )
        if select_action:
            self.bind("<<ComboboxSelected>>", select_action)
        self.place(x=xy_cor[0], y=xy_cor[1])

        if default_text != "":
            variable.set(default_text)


class ListBox(Listbox):
    """Listbox widget with integrated scrollbars and item methods."""
    def __init__(self, win, size: tuple, xy_cor: tuple, variable, text_size: int):
        super().__init__(
            win,
            width=size[0],
            height=size[1],
            font=("Helvetica", text_size),
            listvariable=variable,
            yscrollcommand=Scrollbar(win, orient="vertical").set,
            xscrollcommand=Scrollbar(win, orient="horizontal").set
        )
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
    """Warning / Verification alert label with randomized dynamic color highlight."""
    def __init__(self, bg_color: str, text_size: int, text: str, xy_cor: tuple, war_ver: str, win=None):
        master = win if win is not None else None
        super().__init__(master, bg=bg_color, text=text, font=("Times New Roman", text_size))
        if war_ver == "war":
            self.config(fg=f"#{random.choice(colors_warning).lower()}")
        elif war_ver == "ver":
            self.config(fg=f"#{random.choice(colors_verify).lower()}")
        self.place(x=xy_cor[0], y=xy_cor[1])


class CheckButton(Checkbutton):
    """Styled toggle checkbutton with active color states."""
    def __init__(self, win, button_name: str, xy_cor: tuple, bg_color: str, textcolor: str,
                 text_size: int, variable, button_action=None, on_val=1, off_val=0):
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
            onvalue=on_val,
            offvalue=off_val
        )
        self.place(x=xy_cor[0], y=xy_cor[1])


__all__ = [
    "Branding_Text",
    "DynamicPanel",
    "TextLabel",
    "Panel_Tag",
    "SButton",
    "RadioButton",
    "TextEntry",
    "LongEntry",
    "ScrollEntry",
    "DropDown",
    "ListBox",
    "WarVer",
    "CheckButton",
    "colors_warning",
    "colors_verify"
]
