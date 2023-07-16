#!/usr/bin/python3
"""python command line program for my models"""
import cmd
"""A program that contains the entry point of the command interpreter

    class:
        HBNBCommand: inherits from the Cmd class
"""


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        """override the parent emptyline method from executing the
        previous command by excuting nothing
        """
        pass

    def do_quit(self, args):
        """return true to exit the shell"""
        return True

    def do_EOF(self, args):
        """to exit the program using shell shortcut"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
