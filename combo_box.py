#Calling and naming the class library
import tkinter as tk
from tkinter import ttk


#Setting the argument parameter 
def on_select(event):
    
    selected_item = event.widget.get()
    print("Selected item:", selected_item)
    
#Title for the root window
root = tk.Tk()
root.title("Combobox Example")