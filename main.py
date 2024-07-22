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

    list1 = [random.choice(letters) for x in range(nr_letters)]
    list2 = [random.choice(numbers) for x in range(nr_numbers)]
    list3 = [random.choice(symbols) for x in range(nr_symbols)]
    password_list = list1 + list2 + list3
    random.shuffle(password_list)

    password = "".join(password_list)

    pw_entry.delete(0, END)
    pw_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pw_entry.get()
    dict= {website: {"email": email, "password": password}}
    # website = key . value = dictionary . Insided that dictionary you have keys email and pw

    if(len(website) == 0 or len(password) == 0):
        messagebox.showinfo(title="Error", message="Cannot leave any field empty.")

    else:
        try:
            with open("data.json", "r") as file:
                # Read the current data into a dictionary
                data = json.load(file)
                # Add new data to the dictionary loaded
                data.update(dict)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(dict, file, indent=4)
        else:
            with open("data.json", "w") as file:
                # Write this new data / Dict to the JSON file
                json.dump(data, file, indent=4)
        web_entry.delete(0, 'end')
        pw_entry.delete(0, 'end')
# ---------------------------- UI SETUP ------------------------------- #
def find_password():
    website_name = web_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            website_details= data[website_name]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Error", message="No details for the website exists")
    else:
        website_email = website_details["email"]
        website_password = website_details["password"]
        messagebox.showinfo(title=website_name, message=f"Email : {website_email} \n Password : {website_password}")
        print(website_email)
        print(website_password)


# Main window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas containing the actual image
canvas = Canvas()
# canvas["bg"] = "yellow"
canvas["width"] = 200
canvas["height"] = 200
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label()
website_label["text"] = "Website:"
website_label.grid(row=1, column=0)

email_label = Label()
email_label["text"] = "Email/Username:"
email_label.grid(row=2, column=0)

pw_label = Label()
pw_label["text"] = "Password:"
pw_label.grid(row=3, column=0)

# Entries
web_entry = Entry()
web_entry["width"] = 33
web_entry.focus()
web_entry.grid(row=1, column=1)

email_entry = Entry()
email_entry["width"] = 52
email_entry.insert(0, "inamsyed2020@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

pw_entry = Entry()
pw_entry["width"] = 33
pw_entry.grid(row=3, column=1)

# Buttons
pw_button = Button()
pw_button["text"] = "Generate Password"
pw_button["width"] = 14
pw_button["command"] = generate_password
pw_button.grid(row=3, column=2)

add_button = Button()
add_button["text"] = "Add"
add_button["width"] = 44
add_button["command"] = save
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button()
search_button["text"] = "Search"
search_button["width"] = 14
search_button["command"] = find_password
search_button.grid(row=1, column=2)











window.mainloop()
