import msvcrt
import os
import subprocess
from pathlib import Path


IP = ''
ADB_PATH = 'adb'
DESTINATION = '.'

# Check connection.
while os.system(f'{ADB_PATH} connect {IP}'):
    input('Connection failed, press Enter to try again.')

# Magick code '\033[2K\033[1G' to clear current line and move to the start.
prompt = '\033[2K\033[1G' 'fetch> '
buffer = '/sdcard/'
candidate = []

while True:
    print(prompt + buffer, end='', flush=True)
    # flush must be True or nothing will be printed
    key = msvcrt.getwch()
    # getwch instead of getch so that most characters will be captured once
    if key == '\x03':  # backspace
        exit()
    elif key == '\x00' or key == '\xe0':  # special control keys
        key = msvcrt.getwch()
        print('\nInvalid input.')
    elif key == '\t':  # tab to autocomplete
        path = Path(buffer)
        if buffer[-1] == '/':
            folder = path
            name = ''
        else:
            folder = path.parent
            name = path.name

        if candidate:
            buffer = (
                folder / candidate[(candidate.index(name) + 1) % len(candidate)]).as_posix()
        else:
            with subprocess.Popen(f'{ADB_PATH} shell ls {folder.as_posix()}', shell=True, stdout=subprocess.PIPE) as ls:
                ls.wait()
                output = [x.decode().strip() for x in ls.stdout.readlines()]
            for x in output:
                if x[:len(name)] == name:
                    candidate.append(x)
            if candidate:
                buffer = (folder / candidate[0]).as_posix()
            else:
                print('\n' + '\n'.join(output))
    elif key == '\r':  # enter
        print('\nStart pulling...')
        if buffer == '/sdcard/':
            print('Attempting to fetch root, aborted.')
            continue
        if not os.system(f'{ADB_PATH} pull -a "{buffer}" {DESTINATION}'):
            break
    elif key == '\x08':  # ctrl-c
        if len(buffer) > 8:
            buffer = buffer[:-1]
            candidate = []
    else:  # ordinary letters
        buffer += key
        candidate = []
