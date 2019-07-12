import configparser
import os
import shutil

def selectCommand(args):
    config = configparser.ConfigParser()
    config.read('config.ini')

    rc_path = os.path.expanduser(config['Vim']['local_rcs'] + f'/{args["rc"]}')
    shutil.copyfile(rc_path, os.path.expanduser(config['Vim']['vimrc']))
