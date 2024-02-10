#!/usr/bin/python3
import cmd
import json
from uuid import uuid4


class CommandInterpreter(cmd.Cmd):
    """Command line interpreter"""
    prompt = "AirBnB>>> "

    def __init__(self):
        super().__init__()
        self.users = {}  # Empty dictionary to store users
        self.users_file = "users.json"  # file to store data
        self.show_data_in_json()
    # Opens a json file aind reads the info inside it.

    def show_data_in_json(self):
        try:
            with open(self.users_file, "r") as file:
                self.users = json.load(file)
        except FileNotFoundError:
            pass

    # Saves info to a json file
    def save_data_to_json(self):
        with open(self.users_file, "w") as file:
            json.dump(self.users, file)

    # Creates new user
    def do_create_user(self, command):
        """Create new user. Syntax: create_user  <FirstName> <LastName>"""
        args = command.split()
        if len(args) != 2:
            print("Usage: create_user <FirstName> <LastName>")
            self.save_data_to_json()
        else:
            first_name, last_name = args
            user_id = str(uuid4())
            self.users[user_id] = {"first_name": first_name,
                                   "last_name": last_name}
            print(f"User {first_name} {last_name} created")

    # reads users in the file
    def do_read_users(self, command):
        """Read users. Syntax: read_users"""
        if self.users:
            print("Users:")
            for user_id, user_info in self.users.items():
                print(f"ID: {user_id} "
                      f"First Name: {user_info['first_name']} "
                      f"Last Name: {user_info['last_name']}")
                self.show_data_in_json()
        else:
            print("No users found")

    # updates user info
    def do_update_user(self, command):
        """Update user. Syntax: update_user <ID> <FirstName> <LastName>"""
        args = command.split()
        if len(args) != 3:
            print("Usage: update_user <ID> <FirstName> <LastName>")
        else:
            user_id, first_name, last_name = args
            if user_id in self.users:
                self.users[user_id] = {"first_name": first_name,
                                       "last_name": last_name}
                print(f"User with ID {user_id} "
                      f"updated to {first_name} {last_name}")
                self.save_data_to_json()
            else:
                print(f"User with ID {user_id} doesnot exist")

    # deletes a user
    def do_delete_user(self, command):
        """Delete user. Syntax: delete_user <ID>"""
        args = command.split()
        if len(args) != 1:
            print("Usage: delete_user <ID>")
        else:
            user_id = args[0]
            if user_id in self.users:
                del self.users[user_id]
                print(f"User with ID {user_id} deleted")
                self.save_data_to_json()
            else:
                print(f"User with ID {user_id} doesnot exist")

    # exits the command line
    def do_exit(self, arg):
        """Exit the command line interpreter"""
        print("Exiting AirBnB..............")
        return True

    def do_quit(self, arg):
        """Alias for the 'exit' command"""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        """Handle the End-of-file character"""
        print("\n Exiting AirBnB............")
        return True

    # handles unknown commands
    def default(self, line):
        """Handle Unknown Commands"""
        print(f"Unknown command {line}. Type 'help' for available commands.")


if __name__ == "__main__":
    CommandInterpreter().cmdloop()
