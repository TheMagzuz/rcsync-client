#!/usr/bin/env python3
"""RCSync

Usage:
    rcsync.py login [<username>] [<password>]

Options:
    -h --help   Show this screen
    --version   Show version
"""
from docopt import docopt
import requests
import getpass
import configparser
import jwTokens

config = configparser.ConfigParser()

config.read('config.ini')
server_address = config['Server']['server_address']

def loginCommand():
    if args['username']:
        if not args['password']:
            password = loginPrompt(True)
        else:
            password = args['password']
        username = args['username']
    else:
        username, password = loginPrompt(False)
    longToken = durationPrompt()

    login(username, password, longToken)

def loginPrompt(usernameGiven):
    if usernameGiven:
       return getpass.getpass()
    else:
        return input('Username: '), getpass.getpass()

def durationPrompt():
    duration = input('Would you like your login to be remembered for one day? [y/N] ')
    return duration == 'y'

def login(username, password, longToken):
    res = requests.post(server_address + '/users/login', data = {'username': username, 'password': password, 'rememberMe': longToken})

    if res.status_code == 401:
        print('Invalid login')
        return False
    elif res.status_code != 200:
        print('Something went wrong! Error code ' + res.status_code)
        return False

    token = res.text[1::][0:-1:]

    with open('token.dat', 'w') as tokenFile:
        tokenFile.write(token)

    print('Logged in as ' + username)

    return True

def stripAngleBrackets(string):
    if string[0] == '<':
        string = string[1::]
    if string[-1] == '>':
        string = string[0:-1:]
    return string

commands = {
    'login': loginCommand
}


args = docopt(__doc__, version='RCSync Client 0.1')

# Make the arguments list not garbage
args = {stripAngleBrackets(key): value for (key, value) in args.items()}

commandFound = False

# Loop through all the possible commands
for key in commands.keys():
    # Find the entered command
    if args[key] == True:
        commandFound = True
        commands[key]()

if not commandFound:
    print("Unable to find a valid command handler")
