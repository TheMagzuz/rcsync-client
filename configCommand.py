import shutil
import configparser
import os.path

defaultConfig = configparser.ConfigParser()
defaultConfig.read('defaultConfig')

def configCommand(args):
    if os.path.isfile('config.ini'):
        cont = input('A config file already exists. This will be overwritten if you continue. Continue anyway? [y/N] ')
        if cont != 'y':
            return

    if args['--default']:
        shutil.copyfile('defaultConfig', 'config.ini')
        return
    else:
        print('Enter values or empty for default')
        config = configparser.ConfigParser()

        for sectionKey, section in defaultConfig.items():
            if sectionKey == 'DEFAULT':
                continue

            config.add_section(sectionKey)

            for key in section.keys():
                config.set(sectionKey, key, input(f'{key} ({defaultConfig[sectionKey][key]}): ') or defaultConfig[sectionKey][key])
        with open('config.ini', 'w') as configFile:
            config.write(configFile)

