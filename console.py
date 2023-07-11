#!/usr/bin/python3
import cmd
import readline
'''A program that contains the entry point of the command interpreter

    class:
        HBNBCommand: inherits from the Cmd class
'''
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
