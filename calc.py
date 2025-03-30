"""calc.py

This module contains functions and implementations to support
add
sub
mul
div
mod

usage:
* python calc.py add 1 2
  3
* python calc.py sub 4 2
  2
"""
import sys

class InvalidArgs(Exception):
    pass

def main(args):
    if len(args)!=3:
        raise InvalidArgs
    opration = args[0]
    temp_args = args[1::]
    args = [int(args) for args in temp_args]
    if opration.lower() == 'add':
        print(args[0] + args[1])
    elif opration.lower() == 'sub':
        print(args[0] - args[1])
    elif opration.lower() == 'mul':
        print(args[0] * args[1])
    elif opration.lower() == 'div':
        print(args[0] // args[1])
    elif opration.lower() == 'mod':
        print(args[0] % args[1])
    else:
      print("unsupported opration{opration}")

if __name__ == '__main__':
    args = sys.argv[1::]
    try:
        main(args)
    except InvalidArgs:
        print("############################")
        print("Usage is as shown below")
        print("python calc.py add 1 2")
        print("Supported operations are add sub mul div mod")
