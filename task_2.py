class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        # Validate phone number format
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


# Test the implementation
if __name__ == "__main__":
    # Creation of a new address book
    book = AddressBook()

    # Creation of a entry for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Add a John entry to the address book
    book.add_record(john_record)

    # Creating and adding a new entry for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Displaying all entries in the contact list
    for name, record in book.data.items():
        print(record)

    # Find and edit a phone number for John
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")

    print(john)  # Displaying: Contact name: John, phones: 1112223333; 5555555555

    # Searching for a specific phone number in John's entry
    if john:
        found_phone = john.find_phone("5555555555")
        if found_phone:
            print(f"{john.name}: {found_phone}")
        else:
            print("Phone number not found")

    # Deletion Jane's entry
    book.delete("Jane")