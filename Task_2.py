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

        elif command == "add ":
            if len(args) != 2:
                print("Invalid command format. Use 'add [name] [phone number]'.")
            else:
                name, phone = args
                contacts[name] = phone
                print("Contact added.")

        elif command == "change":
            if len(args) != 2:
                print("Invalid command format. Use 'change [name] [new phone number]'.")
            else:
                name, new_phone = args
                if name in contacts:
                    contacts[name] = new_phone
                    print("Contact updated.")
                else:
                    print("Contact not found.")

        elif command == "phone":
            if len(args) != 1:
                print("Invalid command format. Use 'phone [name]'.")
            else:
                name = args[0]
                if name in contacts:
                    print(contacts[name])
                else:
                    print("Contact not found.")

        elif command == "all":
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
