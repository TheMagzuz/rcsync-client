import requests
import getpass
import configparser
import jwTokens
import os

def loginCommand(args):
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
    config = configparser.ConfigParser()
    config.read('config.ini')
    server_address = config['Server']['server_address']

    res = requests.post(server_address + '/users/login', data = {'username': username, 'password': password, 'rememberMe': longToken})

    if res.status_code == 401:
        print('Invalid login')
        return False
    elif res.status_code != 200:
        print('Something went wrong! Error code ' + str(res.status_code))
        return False

    token = res.text[1::][0:-1:]

    token_path = os.path.expanduser(config['User']['token_path'])
    token_folder = os.path.dirname(token_path)

    if not os.path.exists(token_folder):
        os.makedirs(token_folder)

    with open(token_path, 'w+') as tokenFile:
        tokenFile.write(token)

    print('Logged in as ' + username)

    return True

