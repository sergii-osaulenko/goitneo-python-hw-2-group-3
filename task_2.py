class InvalidPhoneNumberError(ValueError):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise InvalidPhoneNumberError("Phone number must be a 10-digit number.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = {}

    def add_phone(self, phone_number):
        try:
            phone = Phone(phone_number)
            self.phones[phone_number] = phone
            print("Phone added successfully.")
        except InvalidPhoneNumberError as e:
            print(e)

    def remove_phone(self, phone_number):
        if phone_number in self.phones:
            del self.phones[phone_number]
            print("Phone removed successfully.")
        else:
            print("Phone number not found.")

    def edit_phone(self, old_phone_number, new_phone_number):
        if old_phone_number in self.phones:
            try:
                new_phone = Phone(new_phone_number)
                self.phones[new_phone_number] = self.phones.pop(old_phone_number)
                print("Phone number edited successfully.")
            except InvalidPhoneNumberError as e:
                print(e)
        else:
            print("Phone number not found.")

    def find_phone(self, phone_number):
        return self.phones.get(phone_number)

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones.values())
        return f"Contact name: {self.name}, phones: {phones_str}"

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record