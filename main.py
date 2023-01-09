from tkinter import *


# ---------------------------- PASSWORD GENERATOR -------------------------- #
def generate_password():
    print("Password Generated")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    print("Password Added")


# ---------------------------- UI SETUP ------------------------------------ #
DEFAULT_PADDING = {"padx": 10, "pady": 10}

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# WEBSITE
# Website label
web_label = Label(text="Website")
web_label.grid(column=0, row=1)
web_label.config(DEFAULT_PADDING)
# Website entry field
web_entry = Entry(width=45)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

# USERNAME
# Username label
uname_label = Label(text="Email / Username")
uname_label.grid(column=0, row=2)
uname_label.config(DEFAULT_PADDING)
# Username entry field
uname_entry = Entry(width=45)
uname_entry.insert(END, "my@email.com")
uname_entry.grid(column=1, row=2, columnspan=2)

# PASSWORD
# Password label
passwd_label = Label(text="Password")
passwd_label.grid(column=0, row=3)
passwd_label.config(DEFAULT_PADDING)
# Password entry field
passwd_entry = Entry(width=25)
passwd_entry.grid(column=1, row=3)
# Generate password button
passwd_gen_btn = Button(text="Generate Password", command=generate_password)
passwd_gen_btn.grid(column=2, row=3)
# Add password button
passwd_add_btn = Button(text="Add Password", command=add_password, width=42)
passwd_add_btn.grid(column=1, row=4, columnspan=2, pady=10)

window.mainloop()
