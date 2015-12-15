#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
Homework for Forth Interpreter (OOP Approach)
https://github.com/koder-ua/python-classes/blob/master/slides/pdf/FF_tasks.pdf
Slide #15
"""


class Command(object):
    """ Basic class for all Forth commands """
    name = None

    def __init__(self, operand):
        self.operand = operand

    def execute(self, stack):
        pass


class Put(Command):
    """ put: put value in stack  """
    name = "put"

    def execute(self, stack):
        stack.append(self.operand)


class Pop(Command):
    """ pop: pop value from stack """
    name = "pop"

    def execute(self, stack):
        stack.pop()


class Add(Command):
    """ add: addition of two last values fom stack """
    name = "add"

    def execute(self, stack):
        stack.append(stack.pop() + stack.pop())


class Sub(Command):
    """ sub: subtraction of two last values from stack """
    name = "sub"

    def execute(self, stack):
        stack.append(stack.pop() - stack.pop())


class Print(Command):
    """ print: pop from stack and print value  """
    name = "print"

    def execute(self, stack):
        print stack.pop()


class Forth(object):
    def __init__(self, filename, supp_commands):
        """
        :param filename: Forth source file
        :param supp_commands: supported commands
        """
        self.stack = []
        self.filename = filename
        self.supp_commands = supp_commands

    def __parse_file(self):
        with open(self.filename, 'r') as fd:
            for line in fd:
                # Remove leading and trailing whitespaces including
                # command and operand, e.g. "    put    6  \n" --> "put 6"
                line = " ".join(line.strip().split())
                # Reject all comments and empty lines
                if "#" in line or line == "":
                    continue
                # Commands with operand, e.g. put 1
                elif " " in line:
                    # Do only one splitting, because operand can be a string
                    # with spaces, e.g. put "Hello World!"
                    command, operand = line.split(" ", 1)
                    # Remove redundant quotes, e.g. '"High!"' --> "High!"
                    if operand.startswith('"') and operand.endswith('"'):
                        operand = operand[1:-1]
                    # Wrong syntax, e.g. put 4 3; put "Hi" 5; put "4" 12
                    elif " " in operand:
                        raise ValueError("Invalid command syntax")
                    else:
                        operand = int(operand)
                    yield command, operand
                # Single commands, e.g. pop, print, ...
                else:
                    yield line.split()[0], None

    def run(self):
        try:
            for command, operand in self.__parse_file():
                for cmd in self.supp_commands:
                    if command in cmd:
                        # EAFP principle
                        self.supp_commands[cmd](operand).execute(self.stack)
                        break
                else:
                    raise ValueError("Unknown command")
        except IOError as e:
            message = "Error opening file {}.\n{}"
            print message.format(self.filename, e)
        except TypeError as e:
            message = "Math operation error (add, sub).\n{}"
            print message.format(e.message.capitalize())
            raise
        except IndexError as e:
            message = "Command execution error, {}"
            print message.format(e)
            raise


def eval_forth(filename):
    # To add new command just add respective 'class-command'
    # and extend 'supported_commands' dictionary
    supported_commands = {Put.name: Put, Pop.name: Pop, Add.name: Add,
                          Sub.name: Sub, Print.name: Print}
    Forth(filename, supported_commands).run()


def main():
    "main"
    eval_forth("example.frt")
    return 0

if __name__ == "__main__":
    exit(main())
