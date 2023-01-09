from tkinter import *
import random


# ---------------------------- PASSWORD GENERATOR -------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
PASSWORD_LENGTH = 20

num_letters = random.randint(8, 10)
num_numbers = random.randint(4, 6)
num_symbols = PASSWORD_LENGTH - num_letters - num_numbers


def generate_password():
    password_list = []
    for _ in range(num_letters):
        password_list.append((random.choice(LETTERS)))
    for _ in range(num_numbers):
        password_list.append((random.choice(NUMBERS)))
    for _ in range(num_symbols):
        password_list.append((random.choice(SYMBOLS)))

    # Shuffle list and join into a string
    random.shuffle(password_list)
    password = ''.join(password_list)

    # Display password in password entry field
    passwd_entry.delete(0, END)
    passwd_entry.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    # Collect data from entry fields
    website = web_entry.get()
    username = uname_entry.get()
    password = passwd_entry.get()

    # Append password file
    with open("passwords.txt", "a") as file:
        file.write(f"{website}  |  {username}  |  {password}\n")

    # Clear the website and password entry fields
    web_entry.delete(0, END)
    web_entry.focus()
    passwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------------ #
DEFAULT_PADDING = {"padx": 10, "pady": 10}

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
logo = PhotoImage(file="img/logo.png")
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
