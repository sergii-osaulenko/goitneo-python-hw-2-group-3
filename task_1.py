def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please provide a valid name and phone number."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter a valid command."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact '{name}' updated."
    else:
        return f"Contact '{name}' not found."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number: {contacts[name]}"
    else:
        return f"Contact '{name}' not found."

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()