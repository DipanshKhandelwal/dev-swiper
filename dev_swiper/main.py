"""
usage: swipe [-m] [-c COUNT] [-d DIRECTION] [-U]

optional arguments:
  -m, --manual                Manual Swiping
  -c, --count COUNT           Number of swipes                                            [default: 20]
  -d, --direction DIRECTION   Swipe direction : { 'l' , 'left', 'r', 'right }   [default: right]
  -U, --update                Update this program to latest version.
  -V, --version               Print application version
  -h, --help                  show this help message and exit
"""

import sys
import os
import curses

from docopt import docopt, DocoptExit
from dev_swiper import __version__


def update():
    """Runs the upgrade command and upgrades dev-swiper"""
    os.system("pip install --upgrade dev-swiper")


def swipe_right():
    os.system("adb shell input swipe 400 500 800 600 60")


def swipe_left():
    os.system("adb shell input swipe 800 500 400 600 60")


def swipe_manually():
    try:
        os.system("adb devices")
    except:
        print("adb not installed. https://developer.android.com/studio/command-line/adb")
        return

    try:
        devices_present = os.system('adb get-state 1>/dev/null 2>&1')
        if devices_present:
            print("No connected devices.")
            return
    except:
        print("adb not installed. https://developer.android.com/studio/command-line/adb")
        return

    screen = curses.initscr()  # get the curses screen window
    curses.noecho()  # turn off input echoing
    curses.cbreak()  # respond to keys immediately (don't wait for enter)
    screen.keypad(True)  # map arrow keys to special values

    screen.addstr(0, 0, 'Enter q to Quit. Press right/left keys to swipe.')

    try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_RIGHT:
                screen.addstr(1, 0, 'right')
                swipe_right()
            elif char == curses.KEY_LEFT:
                screen.addstr(1, 0, 'left ')
                swipe_left()
    finally:
        # shut down cleanly
        curses.nocbreak()
        screen.keypad(0)
        curses.echo()
        curses.endwin()
        print("Closing. Hope you found a match :)")


def swipe_automatically(args=None):
    direction = 'right'
    if args['--direction'] not in ['l', 'left', 'r', 'right']:
        print(
            'Wrong input for direction. Please select from ["l", "left", "r", "right"]')
        return
    else:
        direction = args['--direction']

    count = 20
    try:
        count = int(args['--count'])
    except ValueError:
        raise ValueError('Please input number for swipe count') from None

    if direction in ['l', 'left']:
        for _ in range(count):
            swipe_left()
    elif direction in ['r', 'right']:
        for _ in range(count):
            swipe_right()


def start(args=None):
    if(args['--manual']):
        swipe_manually()
    else:
        swipe_automatically(args)


def run():
    try:
        args = docopt(__doc__, version=__version__)
    except DocoptExit:
        print(__doc__)
        sys.exit(1)

    if args["--update"]:
        update()
    else:
        start(args)


if __name__ == '__main__':
    run()
