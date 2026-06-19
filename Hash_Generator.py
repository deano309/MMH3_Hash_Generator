import customtkinter as ctk
import mmh3
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def generate_hash(event=None):
    text = input_box.get()
    hash_value = mmh3.hash(text, signed=False)

    output_box.configure(state="normal")
    output_box.delete(0, "end")
    output_box.insert(0, f"0x{hash_value:08X}")
    output_box.configure(state="readonly")

def copy_hash():
    value = output_box.get()
    if value:
        root.clipboard_clear()
        root.clipboard_append(value)
        root.update()

root = ctk.CTk()

try:
    root.iconbitmap(resource_path("icon.ico"))
except:
    pass

root.title("32-bit MurmurHash3 Generator")
root.resizable(False, False)

ctk.CTkLabel(root, text="Input String").pack(padx=10, pady=(10, 0))

input_box = ctk.CTkEntry(root, width=360, height=30, corner_radius=8)
input_box.pack(padx=10, pady=5)
input_box.bind("<KeyRelease>", generate_hash)


ctk.CTkLabel(root, text="Hash").pack()

output_box = ctk.CTkEntry(
    root,
    width=150,
    height=30,
    corner_radius=8,
    justify="center"
)
output_box.pack(padx=10, pady=(5, 5))
output_box.configure(state="readonly")

ctk.CTkButton(
    root,
    text="Copy",
    command=copy_hash,
    corner_radius=8,
    width=90
).pack(pady=(0, 10))

input_box.focus()
root.mainloop()
