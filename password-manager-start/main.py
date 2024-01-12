from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list1 = [random.choice(letters) for num in range(nr_letters)]
    password_list2 = [random.choice(symbols) for number in range(nr_symbols)]
    password_list3 = [random.choice(numbers) for no in range(nr_numbers)]

    password_list = password_list2 + password_list1 + password_list3
    random.shuffle(password_list)

    password = "".join(password_list)

    password_text_box.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def validation():
    if len(website_text_box.get()) == 0 or len(email_text_box.get()) == 0 or len(password_text_box.get()) == 0:
        messagebox.showinfo(title="Oops", message="One of the field is empty!")
    else:
        add_button_clicked()


def add_button_clicked():
    website = website_text_box.get().title()
    email = email_text_box.get()
    password = password_text_box.get()

    new_data = {website: {
        "email": email,
        "password": password
    }}
    # If there is no data in Json file then the code will throw an exception where is
    # can't read the file in first place therefore there is a try catch block to catch the exception of file not found
    try:
        with open("data.json", "r") as data_file:
            # Reading the old data
            data = json.load(data_file)
            # Updating old data with new data
            data.update(new_data)
    except FileNotFoundError:
        data = new_data
    finally:
        with open("data.json", "w") as data_file:
            # Saving updated dada
            json.dump(data, data_file, indent=4)

            website_text_box.delete(0, END)
            password_text_box.delete(0, END)
            website_text_box.focus()

# ----------------------------- Search -------------------------------- #


def search():
    website = website_text_box.get()
    # opening the json file
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail for {website} exits.")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=20, pady=20)
window.title("Genji's password manager")

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# All label

# Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Email
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entry box

# Website entry box
website_text_box = Entry(width=20)
website_text_box.grid(column=1, row=1)
website_text_box.focus()

# Email entry box
email_text_box = Entry(width=35)
email_text_box.grid(column=1, row=2, columnspan=2)
email_text_box.insert(0, "aumzaveri06@gmail.com")


# Password entry box
password_text_box = Entry(width=19)
password_text_box.grid(column=1, row=3)

# All button

# generate password
generate_password_button = Button(text="Generate Password", width=21, font=("Arial", 5, "normal"),
                                  command=generate_password)
generate_password_button.grid(column=2, row=3)

# add password
add_password = Button(text="Add", width=30, command=validation)
add_password.grid(column=1, row=4, columnspan=2)

# search password
search_password = Button(text="Search", command=search)
search_password.grid(column=2, row=1)

window.mainloop()
