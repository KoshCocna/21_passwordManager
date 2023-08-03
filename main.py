from tkinter import *
<<<<<<< HEAD
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
=======
from random import choice, shuffle, randint


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))
    numbers = list(map(chr, range(48, 58)))
    symbols = list(map(chr, range(33, 48))) + list(map(chr, range(58, 65))) + list(map(chr, range(91, 97))) + list(
        map(chr, range(123, 127)))
    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    random_symbols = [choice(symbols) for _ in range(randint(3, 5))]
    password = random_letters + random_numbers + random_symbols
    shuffle(password)
    password = "".join(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
>>>>>>> 585a6e4 (second commit)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
<<<<<<< HEAD

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
=======
    with open("password.txt", "a") as data_file:
        data_file.write(f"{website} || {email} || {password}\n")
    website_entry.delete(0, END)
    password_entry.delete(0, END)
>>>>>>> 585a6e4 (second commit)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
<<<<<<< HEAD
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
=======
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
>>>>>>> 585a6e4 (second commit)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

<<<<<<< HEAD
# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "kim@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
=======
website_label = Label(text="website")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
email_label = Label(text="email")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.insert(0, "kim@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_label = Label(text="password")
password_label.grid(row=3, column=0)
password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)
generate_btn = Button(text="generate", command=generate_password)
generate_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=15, command=save)
add_btn.grid(row=4, column=1)
>>>>>>> 585a6e4 (second commit)

window.mainloop()
