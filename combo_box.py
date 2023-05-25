#Calling and naming the class library
import tkinter as tk
from tkinter import ttk


#Setting the argument parameter 
def on_select(event):
    
    selected_item = event.widget.get()
    print("Selected item:", selected_item)
    
#Title for the root window
root = tk.Tk()
root.title("Favorite Color")

#Create the array
items = ["Red", "Green", "Purple", "Orange"]

#Creating the combobox object with array values in it and placing it in root window
combo_box = ttk.Combobox(root, values=items)
#Binding event to the on_selected function
combo_box.bind("<<ComboboxSelected>>", on_select)

#Putting the object on the display
combo_box.pack()

#Keeping the root window open
root.mainloop()
