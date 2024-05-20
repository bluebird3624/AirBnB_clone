#!/usr/bin/python3
"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_quit(self,line):
        """
        Command to Exit the program
        """
        return True
    def do_EOF(self,line):
        """
        Signal to Exit the program
        """
        return True
    def emptyline(self,line) -> bool:
        pass

    def default(self, line):
        """
        Handles unkown cmmands
        """
        print(f"Unknown Command {line}")

    def do_create(self,line):
        """
                                    Description
        -----------------------------------------------------------------------------------
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        -----------------------------------------------------------------------------------
                                 Usage
        -----------------------------------------------------------------------------------
        $ create BaseModel
        -----------------------------------------------------------------------------------
                                    Return
        -----------------------------------------------------------------------------------
        If the class name is missing, print ** class name missing ** (ex: $ create)
        If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel) 
        """

        class_name = line.split()[0] if line else None  # Extract the class name from the command line
        if not class_name:
            print("** class name missing **")
            return
        
        # Check if the specified class exists in the models module
        if class_name not in dir(models):
            print("** class doesn't exist **")
            return
        
        # Create a new instance of the specified class
        new_instance = getattr(models, class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class_name> <id>
        Example: show BaseModel 1234-1234-1234
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in dir(models):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_instances = models.storage.all()

        instance_key = class_name + '.' + instance_id
        if instance_key not in all_instances:
            print("** no instance found **")
            return

        instance = all_instances[instance_key]
        print(instance)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (saves the change into the JSON file).
        Usage: destroy <class_name> <id>
        Example: destroy BaseModel 1234-1234-1234
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in dir(models):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        all_instances = models.storage.all()

        instance_key = class_name + '.' + instance_id
        if instance_key not in all_instances:
            print("** no instance found **")
            return

        del all_instances[instance_key]
        models.storage.save()

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        Usage: update <class_name> <id> <attribute_name> <attribute_value>
        Example: update BaseModel 1234-1234-1234 name "John"
        """
        args = line.split()
        if len(args) < 3:
            print("Usage: update <class_name> <id> <attribute_name> <attribute_value>")
            return

        class_name = args[0]
        if class_name not in dir(models):
            print("** class doesn't exist **")
            return

        instance_id = args[1]
        all_instances = models.storage.all()
        instance_key = class_name + '.' + instance_id

        if instance_key not in all_instances:
            print("** no instance found **")
            return

        instance = all_instances[instance_key]

        attribute_name = args[2]
        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** can't update {} **".format(attribute_name))
            return

        attribute_value = " ".join(args[3:])

        try:
            attribute_value = eval(attribute_value)  # Evaluate the attribute value to handle strings, integers, and floats
        except (NameError, SyntaxError):
            pass  # If the value cannot be evaluated, treat it as a string

        setattr(instance, attribute_name, attribute_value)
        models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()