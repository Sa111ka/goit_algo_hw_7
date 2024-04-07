from collections import defaultdict, UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    # реалізація класу
    pass

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)  # TODO: check
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if len(value) == 10 and value.isdigit():
            self.__value = value
        else:
            raise ValueError('Invalid phone number')


class Birthday(Field):
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value)
        except ValueError:
            pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        # Phone('0951111111') == '0951111111'
        self.phones = [p for p in self.phones if str(p) != phone_number]

    # TODO: Потрібно додати функції з попередньої роботи

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        # Put your logic here
        pass

    def find_next_birthday(self, weekday):
        pass

    def get_upcoming_birthday(self, days=7):
        pass


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError"
        except ValueError:
            return "ValueError"
        except IndexError:
            return "IndexError"
    return wrapper


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
@input_error
def change_contact(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    if record:
        record.remove_phone(phone)
        record.add_phone(phone)
        return "Contact updated."
    else:
        return "Contact not found."


@input_error
def show_phones(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        if record.phones:
            return f"Phone number(s) for {name}: {', '.join(str(p) for p in record.phones)}"
        else:
            return f"No phone number found for {name}."
    else:
        return "Contact not found."



@input_error
def show_all(book: AddressBook):
    if book:
        return "\n".join([str(record) for record in book.values()])
    else:
        return "Address book is empty."

# In Record class
def add_birthday(self, birthday):
    self.birthday = Birthday(birthday)

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        return "Contact not found."

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{record.name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"
    else:
        return "No birthday found for the contact."

@input_error
def birthdays(args, book: AddressBook):
    upcoming_birthdays = [record for record in book.values() if record.birthday and (record.birthday.date - datetime.now().date()).days <= 7]
    if upcoming_birthdays:
        return "\n".join([f"{record.name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}" for record in upcoming_birthdays])
    else:
        return "No upcoming birthdays."


def parse_input(user_input):
    parts = user_input.split()
    command = parts[0].lower().strip()
    args = parts[1:]
    return command, args


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            # реалізація
            pass

        elif command == "phone":
            # реалізація
            pass

        elif command == "all":
            # реалізація
            pass

        elif command == "add-birthday":
            # реалізація
            pass

        elif command == "show-birthday":
            # реалізація
            pass

        elif command == "birthdays":
            # реалізація
            pass

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()