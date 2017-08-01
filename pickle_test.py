import pickle
import os.path


def add_contact(contacts):
    new_name = input("Please type a name: ")
    contacts.append(new_name)
    print("Contact added")
    contacts.sort()
    return contacts


def delete_contact(contacts):
    if not contacts:
        print("There's no contact to delete")
        return contacts
    else:
        print_contact_list(contacts)
        try:
            idx = int(input("Please type the index of the contact you want to delete: "), 10)
            if idx in range(0, len(contacts)):
                del contacts[idx]
            else:
                print("Contact not found")
            return contacts
        except ValueError:
            print("Please only type numbers")


def print_contact_list(contacts):
    if not contacts:
        print("No contact to show")
    else:
        for i, name in enumerate(contacts):
            print(' (', i, ') ', name)


def save(contacts):
    if not contacts:
        print("No contact to save")
        return
    with open('save_file.pkl', 'wb') as output:
        pickle.dump(contacts, output)
    print("Contacts saved")


def load():
    try:
        with open('save_file.pkl', 'rb') as source:
            contacts = pickle.load(source)
        print("Contacts loaded")
        return contacts
    except FileNotFoundError:
        print("Save file not found")


def main():

    contact_list = []

    while True:

        print('''
        What do you want to do?
          (A)dd name
          (D)elete name
          S(e)e all contacts
          (S)ave
          (L)oad
          (C)lose program
        ''')

        choice = input().lower()

        if choice == 'a':
            contact_list = add_contact(contact_list)

        elif choice == 'd':
            contact_list = delete_contact(contact_list)

        elif choice == 'e':
            print_contact_list(contact_list)

        elif choice == 's':
            save(contact_list)

        elif choice == 'l':
            contact_list = load()

        elif choice == 'c':
            break

        else:
            print("Invalid choice")

main()
