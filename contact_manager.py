def add_contact(contacts):
	new_contact = input("Type the contact name: ")
	contacts.append({
		"name": new_contact,
		"favorite": False
	})
	print("New contact added!")
	return

def show_contacts(contacts):
	print("\nContact list:")
	for index, contact in enumerate(contacts, start=1):
		contact_name = contact["name"]
		print(f"{index}. {contact_name}")
	return

def edit_contact(contacts):
	show_contacts(contacts)
	contact_index = int(input("Please type the contact number you want to update: "))

	if contact_index > 0 and contact_index <= len(contacts):
		new_contact_name = input("Please type the new name: ")
		contacts[contact_index - 1]["name"] = new_contact_name
		print("Contact updated!")
	else:
		print("Contact number does not exist!")
	return

def toggle_favorite_contact(contacts):
	show_contacts(contacts)
	contact_index = int(input("Please type the contact number you want to set/unset as favorite: "))

	if contact_index > 0 and contact_index <= len(contacts):
		contacts[contact_index - 1]["favorite"] = not contacts[contact_index - 1]["favorite"]
		print("Contact updated!")
	else:
		print("Contact number does not exist!")
	return

def show_favorite_contacts_list(contacts):
	print("\nFavorite contact list:")
	for contact in contacts:
		if contact["favorite"]:
			print(contact["name"])
	return

def remove_contact(contacts):
	show_contacts(contacts)
	contact_index = int(input("Please type the contact number you want to delete: "))

	if contact_index > 0 and contact_index <= len(contacts):
		contacts.remove(contacts[contact_index - 1])
		print("Contact deleted!")
	else:
		print("Contact number does not exist!")
	return

contacts = []

while True:
	print("\nWelcome to the Contact Manager project!")
	print("1. Add a contact")
	print("2. Show your contact list")
	print("3. Edit a contact")
	print("4. Set/unset a contact as favorite")
	print("5. Show your contact favorite list")
	print("6. Delete a contact")
	print("7. Exit")

	choice = input("Select an option: ")

	if choice == "1":
		add_contact(contacts)
	if choice == "2":
		show_contacts(contacts)
	if choice == "3":
		edit_contact(contacts)
	if choice == "4":
		toggle_favorite_contact(contacts)
	if choice == "5":
		show_favorite_contacts_list(contacts)
	if choice == "6":
		remove_contact(contacts)
	if choice == "7":
		print("\nSee you soon!")
		break
