#!/usr/bin/env python3
"""RCSync

Usage:
    rcsync.py login [<username>] [<password>]

Options:
    -h --help   Show this screen
    --version   Show version
"""
from docopt import docopt
from loginCommand import loginCommand

commands = {
    'login': loginCommand
}

def stripAngleBrackets(string):
    if string[0] == '<':
        string = string[1::]
    if string[-1] == '>':
        string = string[0:-1:]
    return string

args = docopt(__doc__, version='RCSync Client 0.1')

# Make the arguments list not garbage
args = {stripAngleBrackets(key): value for (key, value) in args.items()}

commandFound = False

# Loop through all the possible commands
for key in commands.keys():
    # Find the entered command
    if args[key] == True:
        commandFound = True
        commands[key](args)

if not commandFound:
    print("Unable to find a valid command handler")
