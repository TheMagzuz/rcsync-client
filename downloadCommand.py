import requests
import configparser
import jwTokens
import os

def downloadCommand(args):
    config = configparser.ConfigParser()
    config.read('config.ini')

    if jwTokens.token():
        res = requests.get(config['Server']['server_address'] + f'/rc/{args["owner"]}/{args["id"]}', headers={'Authorization': 'Bearer ' + jwTokens.token()})
    else:
        res = requests.get(config['Server']['server_address'] + f'/rc/{args["owner"]}/{args["id"]}')

    rc_name = f'{args["owner"]}-{args["id"]}'

    name_input = input(f'Enter the name of the rc (Blank for {rc_name}): ')

    if name_input:
        rc_name = name_input

    rc_path = os.path.expanduser(config['Vim']['local_rcs'] + f'/{rc_name}')
    rc_folder = os.path.dirname(rc_path)

    if not os.path.exists(rc_folder):
        os.makedirs(rc_folder)

    with open(rc_path, 'w+') as rcFile:
        rcFile.write(res.text)

    print('Rc saved as ' + rc_name)
