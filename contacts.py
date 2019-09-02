contacts = [
   {
       "name": "John",
       "phone": "123456"
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

FORMAT_STR = "{:<12} {:>12}"


def print_contact(contact):
    print(FORMAT_STR.format(
        contact['name'], 
        contact['phone']
    ))


def list_contacts(contacts):
    print(FORMAT_STR.format('Name', 'Phone'))
    for contact in contacts:
        print_contact(contact)


def nice_input(message):
    print(message + ':')
    result = input("> ")
    return result


def find_contact(contacts, name=None):
    if not name:
        name = nice_input("Введите имя контакта")

    for contact in contacts:
        if contact['name'] == name:
            return contact
    return None


def show_contact(contacts):
    contact = find_contact(contacts)
    if contact is not None:
        print_contact(contact)
    else:
        print("Контакт не найден")


def add_contact(contacts):
    name = nice_input("Введите имя контакта")
    contact = find_contact(contacts, name)
    if contact:
        print("Такой контакт уже существует!")
    else:
        phone = nice_input("Введите телефон контакта")
        new_contact = {
            'name': name,
            'phone': phone
        }
        contacts.append(new_contact)
        print_contact(new_contact)


def edit_contact(contacts):
    contact = find_contact(contacts)
    if contact:
        new_name = nice_input("Введите новое имя контакта")
        new_phone = nice_input("Введите новый телефон контакта")
        
        # if ',' in new_name:
        #     print("Запятую нельзя!")
        #     return

        contact['name'] = new_name
        contact['phone'] = new_phone
        print_contact(contact)
    else:
        print('Контакт не найден!')


def delete_contact(contacts):
    contact = find_contact(contacts)
    if contact:
        contacts.remove(contact)
        print("Контакт удалён!")
    else:
        print('Контакт не найден!')


def help():
    print("""    Команды:
* list - показать список контактов
* find - найти контакт по имени
* add - добавить контакт в книгу
* edit - поменять данные контакта
* delete - удалить контакт
* help - показать список команд
* exit - выход.""")


def handle_command(command):
    if command == 'list':
        list_contacts(contacts)
    elif command == 'find':
        show_contact(contacts)
    elif command == 'add':
        add_contact(contacts)
    elif command == 'edit':
        edit_contact(contacts)
    elif command == 'delete':
        delete_contact(contacts)
    elif command == 'help':
        help()
    else:
        print("Неизвестная команда.")


def main():
    print("Добро пожаловать в телефонную книгу!")
    help()
    while True:
        command = nice_input("\nВведите команду")
        if command == 'exit':
            print("Выход")
            break
        else:
            handle_command(command)


main()
