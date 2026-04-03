import argparse
import sys
import os
import json

CONTACTS_FILE="contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

def save_contact(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent = 2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("contact", type = str, nargs="*", help="Contact to add. Please enter in format: NAME,EMAIL")
    parser.add_argument("-l", "--list", help="List all contacts", action="store_true")
    parser.add_argument("-d", "--delete", type = int, help = "Delete contact by ID")
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    if args.list:
        contacts = load_contacts()
        if len(contacts) == 0:
            print("You have 0 contacts. Add some")
        for contact in contacts:
            print(f"{contact['id']}")
        sys.exit(0)
    elif args.delete:
        contacts = load_contacts()
        new_contacts = []
        for contact in contacts:
            if contact["id"] != args.delete:
                new_contacts.append(contact)
        contacts = new_contacts
        save_contact(new_contacts)
        print(f"Contact with ID of {args.delete} deleted")
    elif args.contact:
        contactInformation = args.contact
        contactInformation = contactInformation[0].split(',')
        name = contactInformation[0]
        email = contactInformation[1]
        contacts = load_contacts()
        if len(contacts)==0:
            new_id=1
        else:
            new_id=contacts[-1]['id']+1
        contacts.append({"id":new_id, "name":name, "email":email})
        save_contact(contacts)
        print(f"Contact {name} along with their email {email} has been added with ID {new_id}")

if __name__ == "__main__":
    main()