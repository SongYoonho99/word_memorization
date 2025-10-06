import tkinter as tk

def center_window(window: tk.Toplevel | tk.Tk, width: int, height: int):
    x = window.winfo_screenwidth() // 2 - width // 2
    y = window.winfo_screenheight() // 2 - height // 2
    window.geometry(f"{width}x{height}+{x}+{y}")