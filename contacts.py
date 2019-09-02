# contacts = [
#    {
#        "name": "John",
#        "phone": "123456"
#    },
#    {
#        "name": "Ruslan",
#        "phone": "07003869"
#    },
#    {
#        "name": "Eddy",
#        "phone": "414443"
#    },
#    {
#        "name": "Jane",
#        "phone": "564321"
#    },
#    {
#        "name": "Bob",
#        "phone": "+1234"
#    },
# ]
contacts = []
def taking_contacts_data():
  print("Reading the file")  
  with open('contacts.txt', 'r') as f:
    for line in f:
      name, phone = line.strip().split(',')
      contact = {
        "name": name,
        'phone': phone
      }
      contacts.append(contact)
  return contacts
taking_contacts_data()
print(contacts)
def write_txt_file(contacts):
  with open('contacts.txt', 'w') as f:
    for item in contacts:
      contact_str = f'{item["name"]},{item["phone"]}\n'
      f.write(contact_str)
  print("file contact.txt is created")
def list_contancts(contacts):
  print()
  format_string =  '{:<15} {:>15}'
  print(format_string.format("Name", "Phone"))
  for contact in contacts:
    print(format_string.format(
      contact["name"], 
      contact['phone']
      ))

def find_contact(contacts):
  format_string =  '{:<15} {:>15}'
  
  print("enter name")
  name = input(">")
  for contact in contacts:
    if contact["name"] ==  name:
      print(format_string.format(
        contact["name"], 
        contact['phone']
      
        ))
      break
  else:
      print('contact not found ')
def add_contact(contacts):
  contact  = {}
  print('Enter the name')
  name = input('> ')
  while True:
    if set(name) & set(',')!=set():
      print('Enter the name, without \',\'')
      name = input('> ')
    else:
      break
  print("Enter Phone-number ")
  Phone = input('> ')
  while True:
    if set(Phone) & set(',')!=set():
      print('Enter the Phone-number, without \',\'')
      Phone = input('> ')
    else:
      break
  contact={
    "name": name,
    "phone": Phone
  }
  contacts.append(contact)
  print("contact is added")
  write_txt_file(contacts)
  print()

print("Welcomre to contact List\n Command")
print(""" 
          * list
          * find
          * add
          * exit
          * file.txt """)
while True:

  print("Enter command")
  command = input(">")
  if command == "list":
    list_contancts(contacts)
  elif command == 'find':
    find_contact(contacts)
  elif command == 'file.txt':
    write_txt_file(contacts)
  elif command == 'add':
    add_contact(contacts)
  elif command == 'exit':
    break
  else:
    print("Command not found")
