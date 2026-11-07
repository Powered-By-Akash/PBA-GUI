"""
PBA-GUI Showcase Demo
=====================
Demonstrates the core visual components of the PBA-GUI framework.
Run:
    python examples/demo.py
"""

import sys
import tkinter as tk
from tkinter import messagebox

# Add parent directory to sys.path if running directly from repo
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pba_gui import (
    Branding_Text,
    DynamicPanel,
    TextLabel,
    Panel_Tag,
    SButton,
    TextEntry,
    DropDown,
    ListBox,
    CheckButton
)


def main():
    root = tk.Tk()
    root.title("PBA-GUI v2025 | Component Showcase")
    root.geometry("640x500")
    root.configure(bg="#0b1120")
    root.resizable(False, False)

    # 1. Header Branding
    Branding_Text(
        win=root,
        bg_color="#0b1120",
        branding_text="POWERED BY AKASH (PBA) - GUI ENGINE 2025",
        fg_color="#00f5ff",
        text_size=12,
        xy_cor=(20, 16)
    )

    # 2. Left Panel (Settings & Controls)
    DynamicPanel(
        win=root,
        panel_size=(290, 410, 2),
        xy_cor=(20, 55),
        panel_bgcolor="#111827",
        panel_border_color="#00d4ff"
    )

    Panel_Tag(
        win=root,
        panel_name=" CONTROL CONSOLE ",
        text_size=10,
        xy_cor=(35, 68)
    )

    TextLabel(
        win=root,
        bg_color="#111827",
        text="Project Name:",
        text_color="#94a3b8",
        font_details=("Segoe UI", 9, "bold"),
        xy_cor=(35, 105)
    )

    entry = TextEntry(
        win=root,
        entry_width=25,
        entry_text="AutoCAD Pipeline v4",
        entry_text_size=10,
        xy_cor=(35, 130)
    )

    TextLabel(
        win=root,
        bg_color="#111827",
        text="Select Module Category:",
        text_color="#94a3b8",
        font_details=("Segoe UI", 9, "bold"),
        xy_cor=(35, 175)
    )

    cat_var = tk.StringVar()
    DropDown(
        win=root,
        select_action=None,
        items=["Drafting Automation", "BOM Extractor", "Batch Plotter", "ERP Bridge"],
        xy_cor=(35, 200),
        box_size=(23, 6),
        text_size=9,
        variable=cat_var,
        default_text="Drafting Automation"
    )

    chk_var = tk.IntVar(value=1)
    CheckButton(
        win=root,
        button_name="Enable High-Speed Buffer",
        xy_cor=(35, 250),
        bg_color="#111827",
        textcolor="#e2e8f0",
        text_size=9,
        variable=chk_var
    )

    def on_launch():
        messagebox.showinfo(
            "PBA-GUI Action",
            f"Launched '{entry.get()}' with module '{cat_var.get()}'!"
        )

    SButton(
        win=root,
        button_size=(22, 2),
        button_color="#00d4ff",
        text_color="#0b1120",
        active_button_color="#38bdf8",
        active_text_color="#ffffff",
        button_name="INITIALIZE PROCESS",
        button_text_size=10,
        button_text="Segoe UI",
        xy_cor=(35, 300),
        button_action=on_launch
    )

    # 3. Right Panel (Telemetry & List)
    DynamicPanel(
        win=root,
        panel_size=(290, 410, 2),
        xy_cor=(330, 55),
        panel_bgcolor="#111827",
        panel_border_color="#ff007f"
    )

    Panel_Tag(
        win=root,
        panel_name=" ACTIVE PIPELINE QUEUE ",
        text_size=10,
        xy_cor=(345, 68)
    )

    list_var = tk.StringVar()
    lb = ListBox(
        win=root,
        size=(27, 10),
        xy_cor=(345, 105),
        variable=list_var,
        text_size=9
    )

    for idx, item in enumerate([
        "[01] AutoCAD Layer Manager v2.4",
        "[02] Dynamic Title Block Sync",
        "[03] UDN Drawing Dispatcher",
        "[04] BOM Excel Generator",
        "[05] Fast Batch Plot PDF"
    ]):
        lb.add_item(idx, item)

    def on_status():
        selected = lb.get_value()
        messagebox.showinfo("Pipeline Status", f"Selected: {selected}")

    SButton(
        win=root,
        button_size=(22, 2),
        button_color="#ff007f",
        text_color="#ffffff",
        active_button_color="#ec4899",
        active_text_color="#ffffff",
        button_name="INSPECT QUEUE ITEM",
        button_text_size=10,
        button_text="Segoe UI",
        xy_cor=(345, 300),
        button_action=on_status
    )

    # If run in non-interactive / headless test mode
    if "--test" in sys.argv:
        root.update()
        root.destroy()
        print("Demo test passed successfully!")
    else:
        root.mainloop()


if __name__ == "__main__":
    main()
