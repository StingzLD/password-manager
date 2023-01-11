from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import pyperclip
import random


# ---------------------------- PASSWORD GENERATOR ---------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
PASSWORD_LENGTH = 20

num_letters = random.randint(8, 10)
num_symbols = random.randint(4, 5)
num_numbers = PASSWORD_LENGTH - num_letters - num_symbols


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


# ---------------------------- SAVE PASSWORD --------------------------------- #
def save_password():
    # Collect data from entry fields
    website = web_entry.get()
    username = uname_entry.get()
    password = passwd_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Information Required",
                            message="Please fill out all fields")
    else:
        try:
            with open("passwords.json", "r") as file:
                # Read the data in the file
                data = json.load(file)
                # Update the data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                # Create new password file and save data
                json.dump(new_data, file, indent=4)
        else:
            with open("passwords.json", "w") as file:
                # Save updated data to password file
                json.dump(data, file, indent=4)
        finally:
            messagebox.showinfo(message="Success!")

        # Clear the website and password entry fields
        web_entry.delete(0, END)
        passwd_entry.delete(0, END)
        web_entry.focus()


# ---------------------------- COPY PASSWORD --------------------------------- #
def copy_password():
    password = passwd_entry.get()
    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    # Collect website from entry field
    website_entered = web_entry.get()
    credentials_not_found = True

    try:
        # Open the password file
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="No password file exists")
    else:
        # Check if website entry field is blank
        if website_entered == "":
            messagebox.showinfo(message="No website was provided")
        else:
            # Loop through websites to find a match
            # Entered text may only be part of the website key
            # E.g., Website Entered: google; Key: google.com
            for website in data.keys():
                # If website entered is in the key string
                if website_entered.lower() in website.lower():
                    credentials_not_found = False
                    creds = data.get(website)
                    messagebox.showinfo(title=website,
                                        message=f"Username: {creds['username']} \n"
                                                f"Password: {creds['password']}")
            if credentials_not_found:
                messagebox.showinfo(message="Credentials Not Found")


# ---------------------------- UI SETUP -------------------------------------- #
DEFAULT_PADDING = {"padx": 10, "pady": 10}
DEFAULT_COLUMN_WIDTH = 10
WINDOW_WIDTH = 675
WINDOW_HEIGHT = 500

# WINDOW
window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=50)
# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# Calculate difference between window and screen dimensions
move_window_right = int(screen_width / 2 - WINDOW_WIDTH / 2)
move_window_down = int(screen_height / 2 - WINDOW_HEIGHT / 2)
# Position window in center of screen
window.geometry(f"+{move_window_right}+{move_window_down}")

# CANVAS
logo_img = PhotoImage(file="img/logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# WEBSITE
# Label
web_label = Label(width=DEFAULT_COLUMN_WIDTH, text="Website")
web_label.grid(column=0, row=1)
web_label.config(DEFAULT_PADDING)
# Entry field
web_entry = Entry(width=45)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2)

# USERNAME
# Label
uname_label = Label(width=DEFAULT_COLUMN_WIDTH, text="Username")
uname_label.grid(column=0, row=2)
uname_label.config(DEFAULT_PADDING)
# Entry field
uname_entry = Entry(width=45)
uname_entry.grid(column=1, row=2, columnspan=2)

# PASSWORD
# Label
passwd_label = Label(width=DEFAULT_COLUMN_WIDTH, text="Password")
passwd_label.grid(column=0, row=3)
passwd_label.config(DEFAULT_PADDING)
# Entry field
passwd_entry = Entry(width=39)
passwd_entry.grid(column=1, row=3)

# SPACER
# Adds additional space in between buttons for better formatting
spacer_label = Label(width=DEFAULT_COLUMN_WIDTH)
spacer_label.grid(column=1, row=5)

# BUTTONS
# Add password
passwd_add_btn = Button(width=38, text="Save Password", command=save_password)
passwd_add_btn.config(highlightbackground="#e5948b", highlightthickness=1)
passwd_add_btn.grid(column=1, row=6, columnspan=2, pady=10)
# Generate password
passwd_gen_btn = Button(width=38, text="Generate Password", command=generate_password)
passwd_gen_btn.config(highlightbackground="#e5948b", highlightthickness=1)
passwd_gen_btn.grid(column=1, row=4, columnspan=2, pady=5)
# Copy password
img = Image.open("img/copy.png")
resized_img = img.resize((17, 17))
copy_img = ImageTk.PhotoImage(resized_img)
copy_btn = Button(width=26, height=26, command=copy_password, image=copy_img)
copy_btn.config(highlightbackground="#e5948b", highlightthickness=1)
copy_btn.grid(column=2, row=3)
# Search for existing password
search_btn = Button(width=38, text="Search for Password", command=search_password)
search_btn.config(highlightbackground="#e5948b", highlightthickness=1)
search_btn.grid(column=1, row=7, columnspan=2)

window.mainloop()
