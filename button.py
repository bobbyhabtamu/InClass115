# Calling and naming the class library
import tkinter as tk

#creating the print function
def button_click():
    print("Button clicked!")
    
# Title on the root window
root = tk.Tk()
root.title("Button Example")

# Creating the button function 
button = tk.Button(root,text="Click Me!", command=button_click)
button.pack()

# Looping the program indefinetly 
root.mainloop()
