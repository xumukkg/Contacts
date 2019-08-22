contacts = [
   {
       "name": "John",
       "phone": "123456"
   },
   {
       "name": "Ruslan",
       "phone": "07003869"
   },
   {
       "name": "Eddy",
       "phone": "414443"
   },
   {
       "name": "Jane",
       "phone": "564321"
   },
   {
       "name": "Bob",
       "phone": "+1234"
   },
]
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
  print("Enter Phone-number ")
  Phone = input('> ')
  contact={
    "name": name,
    "phone": Phone
  }
  contacts.append(contact)
  print("contact is added")
  print()

print("Welcomre to contact List\n Command")
print(""" 
          * list
          * find
          * add
          * exit""")
while True:
  print("Enter command")
  command = input(">")
  if command == "list":
    list_contancts(contacts)
  elif command == 'find':
    find_contact(contacts)
  elif command == 'add':
    add_contact(contacts)
  elif command == 'exit':
    break
  else:
    print("Command not found")
