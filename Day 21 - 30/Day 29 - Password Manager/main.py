import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH FUNCTION ------------------------------- #
def copy_password():
    website = website_field.get()
    with open("data.json", "r") as file:
        data = json.load(file)
    pyperclip.copy(data[website]['password'])

def find_password():
    website = website_field.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            email = data[website]['email']
            password = data[website]['password']
        # tkinter.messagebox.showinfo(title=website, message=data[website]['email'] + "\n" + data[website]['password'])
    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
        tkinter.messagebox.showinfo(title="Error", message="No details for the website exist")
    else:
        info = tkinter.Tk()
        info.title(website)
        info.geometry("250x50")
        tkinter.Button(info, text=email).grid(padx=50)
        tkinter.Button(info, text=password, command=copy_password).grid(sticky="ew", padx=50)
        info.mainloop()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += ([random.choice(letters) for char in range(nr_letters)])

    password_list += [random.choice(symbols) for sym in range(nr_symbols)]

    password_list += [random.choice(numbers) for num in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_field.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_file():
    website = website_field.get()
    email = email_user_field.get()
    password = password_field.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
    else:
        try:
            open("data.json")
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=2)
        else:
            with open("data.json", "r") as file:
                #Reading old data
                data = json.load(file)
                #Updating old data with new data
                data.update(new_data)
            with open("data.json", "w") as file:
                # Saving updated file
                json.dump(data, file, indent=2)
        finally:
            website_field.delete(0, 'end')
            password_field.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
lock_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
website_field = tkinter.Entry(width=35)
website_field.focus()
website_field.grid(column=1, row=1, padx=50)
search_btn = tkinter.Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1, sticky="we")

email_user_label = tkinter.Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)
email_user_field = tkinter.Entry(width=35)
email_user_field.grid(column=1, row=2, padx=50)
email_user_field.insert(0, "shermantaymk@gmail.com")

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)
password_field = tkinter.Entry()
password_field.grid(column=1, row=3,sticky="we",padx=50)
password_btn = tkinter.Button(text="Generate Password", command=generate_password)
password_btn.grid(column=2, row=3)

add_btn = tkinter.Button(text="Add", width=30, command=write_file)
add_btn.grid(column=1, row=4)




window.mainloop()
