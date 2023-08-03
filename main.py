from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("password.txt", "a") as data_file:
                data_file.write(f"{website} || {email} || {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

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

window.mainloop()
