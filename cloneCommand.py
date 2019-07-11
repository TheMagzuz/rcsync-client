import shutil
import os

def cloneCommand(args):

    to_path = os.path.expanduser(config['Vim']['local_rcs'] + f'/{args["to"]}')
    rc_folder = os.path.dirname(to_path)

    if not os.path.exists(rc_folder):
        os.makedirs(rc_folder)

    if os.path.exists(to_path):
        ans = input(f'Rc {args["to"]} already exists are you sure to want to overwrite it? [y/N]: ')

        if ans != 'y':
            return

    if args['from']:
        from_path = os.path.join(rc_folder, args['from'])
        shutil.copyfile(from_path, to_path)
        return
    else:
        shutil.copyfile(os.path.expanduser(config['Vim']['vimrc']), to_path)
        return
