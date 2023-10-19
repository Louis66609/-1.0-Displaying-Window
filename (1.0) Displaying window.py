import customtkinter as ctk
import tkinter
import customtkinter
from PIL import ImageTk, Image
import re

def create_window():
    window = ctk.CTk()
    window.geometry("1400x800")
    ctk.set_appearance_mode("dark")
    window.mainloop()

if __name__ == "__main__":
    create_window()
