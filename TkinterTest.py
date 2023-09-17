import tkinter as tk

# Sets the root for the GUI.
root = tk.Tk()

# Screen size
root.geometry("500x800")
root.title("BW_WOD_GENERATOR_DEMO")

# Creates Title
label = tk.Label(root, text="THIS IS A TEST", font=('MS Gothic', 24))
label.pack(padx=50, pady=50)

tb = tk.Text(root, font=('OCR A Extended', 12))
tb.pack(padx=20)

h_Button = tk.Button(root, text='Click Me!', font=('OCR A Extended', 12))
h_Button.pack(padx=10, pady=10)

root.mainloop()
