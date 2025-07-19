contacts = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append([name, phone, email, address])
    print("Contact added!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for c in contacts:
            print(f"\nName: {c[0]}\nPhone: {c[1]}\nEmail: {c[2]}\nAddress: {c[3]}")

def search_contact():
    search = input("Enter name or phone to search: ")
    for c in contacts:
        if search in c[0] or search in c[1]:
            print(f"\nName: {c[0]}\nPhone: {c[1]}\nEmail: {c[2]}\nAddress: {c[3]}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter name of contact to update: ")
    for c in contacts:
        if c[0] == name:
            c[1] = input("New Phone: ")
            c[2] = input("New Email: ")
            c[3] = input("New Address: ")
            print("Contact updated!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter name of contact to delete: ")
    for c in contacts:
        if c[0] == name:
            contacts.remove(c)
            print("Contact deleted!")
            return
    print("Contact not found.")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Bye! 👋")
        break
    else:
        print("Invalid option.")
