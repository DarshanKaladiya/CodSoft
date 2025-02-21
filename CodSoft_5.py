class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print("Contact added successfully.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print("Contact not found.")

    def update_contact(self, name, new_phone=None, new_email=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        for contact in self.contacts:
            print(contact)


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == '3':
            name = input("Enter name to update: ")
            new_phone = input("Enter new phone (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            contact_book.update_contact(name, new_phone if new_phone else None, new_email if new_email else None)
        elif choice == '4':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            contact_book.display_contacts()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()