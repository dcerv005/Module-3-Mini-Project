
def add_contact(contact_dict):
    try:
        name= input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        email=input("Enter email address: ")
        address= input("Enter home address: ")
        notes= input("Enter notes about the contact: ")
    except Exception as e:
        print(f'Error occurred: {e}')
    
    contact_dict[name.title()]={}
    contact_dict[name.title()]['Phone Number']= phone_number
    contact_dict[name.title()]['Email']= email
    contact_dict[name.title()]['Address']= address
    contact_dict[name.title()]['Notes']= notes
    print(contact_dict)    


def edit_contact(contact_dict):
    try:
        contact= input("Which contact do you want to edit?(Enter Name)").title()
        if contact not in contact_dict:
            raise Exception("Contact does not exist.")
        detail= input("What are you looking to change?(Name/Phone Number/Email/Address/Notes) ").title()
        change= input("To what would you like to change it? ")
        if detail == 'Name':
            contact_dict[change.title()]=contact_dict.pop(contact)
        
        else:
            contact_dict[contact][detail]= change
    
        print(contact_dict)
    except Exception as e:
        print(f"Error: {e}")
        
def delete_contact(contact_dict):
    try:   
        contact= input("Which contact do you want to delete?(Enter Name)").title()
        if contact not in contact_dict:
            print("Contact does not exist.")
        else:
            del contact_dict[contact]
            print(f"Contact: {contact} was deleted.")
    except Exception as e:
        print(f"Error: {e}")

def search_contact(contacts):
    try:    
        contact= input("Which contact are you looking for?(Enter Name)").title()
        if contact in contacts:
            print(f"{contact}:")
            for category, info in contacts[contact].items():
                print(f"\t{category}: {info}")
            
        else:
            print(f"Contact: {contact} does not exist.")
    except Exception as e:
        print(f"Error: {e}")
def display_contacts(contacts):
    if not contacts:
        print("\n\tContact list is empty.")
    for contact in contacts:
        print(f"{contact}")
        for category, details in contacts[contact].items():
            print(f"\t{category}: {details}")
def export_contact(contacts):
    try:
        contact= input("Which contact are you looking to export?(Enter Name)").title()
        type_of_file_action = input("Are you exporting to a new file, (w), or (a)ppending a file?(w/a) ")
        with open('contact_list.txt', type_of_file_action) as file: 
            
            if type_of_file_action == 'a': 
                file.write(f"\n{contact}\n") 
            else:
                file.write(f"{contact}\n")
            for category, item in contacts[contact].items():
                file.write(f"{category}: {item}\n")
             
    except Exception as e:
        print(f"Error: {e}")
def import_contact(contact_dict):    
    try:
        
        file_name=input("Please enter the file_name.txt that you will import contacts from: ") 
        with open(file_name, 'r') as file:
            for line in file:
                if ':' not in line:
                    first_line = line.strip()
                    contact_dict[first_line]={}
                    print(first_line)
                elif ':' in line:
                    category, info = line.strip().split(": ")
                    contact_dict[first_line][category]=info
    except Exception as e:
        print(f"Error occurred: {e}")
contact_dict={}
while True:
    print("\nWelcome to the Contact Management System!\n\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit\n")

    try:
        user_input = int(input("Please select an option from the menu. (1-8) "))
        if user_input == 8:
            print("\n\tClosing Contact Management System...\n")
            break
        elif user_input == 1:
            add_contact(contact_dict)
        elif user_input == 2:
            edit_contact(contact_dict)
        elif user_input == 3:
            delete_contact(contact_dict)
        elif user_input == 4:
            search_contact(contact_dict)
        elif user_input == 5:
            display_contacts(contact_dict)
        elif user_input == 6:
            export_contact(contact_dict)
        elif user_input == 7:
            import_contact(contact_dict)
        else:
            print("Please pick from a number 1-8.")
        

    except Exception as e:
        print(f"Error occurred: {e}")
        print(f"Please enter a number from 1-8.")