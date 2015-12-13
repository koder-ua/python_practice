#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
Homework for Forth Interpreter
https://github.com/koder-ua/python-classes/blob/master/slides/pdf/FF_tasks.pdf
Slide #15
"""


def parse_file(filename):
    """
    Parse and extract forth executable commands line by line,
    comments and empty lines are ignored

    :param filename: file name for parsing
    :return: executable forth command with operand (if exists)
    """
    with open(filename, 'r') as fd:
        for line in fd:
            # Remove leading and trailing whitespaces and whitespaces between
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


def eval_forth(frt_file):
    """
    Forth subset interpreter
    Supported commands: put, pop, add, sub, print
                        # - comment line, "" - empty line

    :param frt_file: Forth format data file
    """
    stack = []
    try:
        for command, operand in parse_file(frt_file):
            if command == "put":
                stack.append(operand)
            elif command == "pop":
                stack.pop()
            elif command == "add":
                stack.append(stack.pop() + stack.pop())
            elif command == "sub":
                stack.append(stack.pop() - stack.pop())
            elif command == "print":
                print stack.pop()
            else:
                raise ValueError("Unrecognized command")
    except IOError as e:
        message = "Error opening file {}.\n{}"
        print message.format(frt_file, e)
    except TypeError as e:
        message = "Math operation error (add, sub).\n{}"
        print message.format(e.message.capitalize())
        raise
    except IndexError as e:
        message = "Command execution error, {}"
        print message.format(e)
        raise


def main():
    "main"
    eval_forth("example.frt")
    return 0


if __name__ == "__main__":
    exit(main())
