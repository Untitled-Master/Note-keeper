import math
import customtkinter
from tkinter import filedialog

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Note keeper")
root.geometry("600x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

label = customtkinter.CTkLabel(frame, text="Note Keeper", font=('Arial', 19))
label.pack()

e1 = customtkinter.CTkEntry(frame, placeholder_text="What do you think...", width=300)
e1.pack(pady=3)

content = customtkinter.CTkTextbox(frame, font=('Robert', 18), width=470)
content.pack(pady=5)

def save_note():
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:
        with open(filename, 'w') as file:
            file.write(content.get("1.0", "end-1c"))

def clear_note():
    content.delete("1.0", "end")

def open_note():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, 'r') as file:
            content.delete("1.0", "end")
            content.insert("1.0", file.read())

btn_frame = customtkinter.CTkFrame(frame)
btn_frame.pack(pady=5)

btn1 = customtkinter.CTkButton(btn_frame, text="Save", command=save_note)
btn1.pack(side="left", padx=5)

btn2 = customtkinter.CTkButton(btn_frame, text="Clear", command=clear_note)
btn2.pack(side="left", padx=5)

btn3 = customtkinter.CTkButton(btn_frame, text="Open", command=open_note)
btn3.pack(side="left", padx=5)

root.mainloop()
