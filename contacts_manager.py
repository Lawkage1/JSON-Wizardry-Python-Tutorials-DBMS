#personal contact manager
import json

def load_contact():
    try:
        with open('contactFile.json', 'r') as f:
            data = json.load(f)
            return data.get('contact', [])
    except Exception as e:
        print(e)
        return []

def save_contacts(contacts):
    with open('contactFile.json', 'w') as file:
        json.dump({'contact': contacts}, file, indent=2)

def add_contacts(contacts):
    name = input("Please enter the name: ")
    try:
        phone = int(input("Please enter phone number: "))
    except Exception as e:
        raise KeyError("please enter valid number")
        return
    email = input("Please enter email: ") + "@gmail.com"
    address = input("Please enter the address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print("Contact added successfully!")

def display_contacts(contacts):
    for contact in contacts:
        print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")
    return

def delete_contacts(contacts):
    name = input("Please enter the name of the person to be deleted: ")
    found = False
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            found = True
            break
    if not found:
        print("Contact not found.")
    return

def update_contacts(contacts):
    name = input("Please enter the name to be updated: ")
    found = False
    for contact in contacts:
        if contact['name'] == name:
            new_name = input("Please enter the new name: ")
            contact['name'] = new_name
            save_contacts(contacts)
            print("Contact updated successfully!")
            found = True
            break
    if not found:
        print("Invalid name.")
    return

def main():
    contacts = load_contact()

    while True:
        print("Here's the menu:\n")
        print("1. Add contact")
        print("2. Update contact")
        print("3. Delete contact")
        print("4. Display contacts")
        print("5. Load stored contacts")
        print("6. Exit the program")

        try:
            choice = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            add_contacts(contacts)
        elif choice == 2:
            update_contacts(contacts)
        elif choice == 3:
            delete_contacts(contacts)
        elif choice == 4:
            display_contacts(contacts)
        elif choice == 5:
            contacts = load_contact()
        elif choice == 6:
            break
        else:
            print("Invalid input! Please enter a number between 1 and 6.")

if __name__ == '__main__':
    main()
