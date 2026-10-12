#!/usr/bin/env python
# /// script
# dependencies = ['pyautogui']
# ///
from time import sleep

from pyautogui import Size
from pyautogui import Point
from pyautogui import position
from pyautogui import size

POLL_INTERVAL_SECONDS: float = 0.5


def trackMouse():
    """
    Tracks and prints mouse coordinates by polling every 0.5 seconds.
    """
    screenSize: Size = size()
    print(f'Screen Size: {screenSize.width}x{screenSize.height}')
    print('Press Ctrl-C to quit.')

    try:
        while True:
            currentLocation: Point = position()
            positionText: str = f'X: {str(currentLocation.x).rjust(4)} Y: {str(currentLocation.y).rjust(4)}'
            print(positionText, end='')
            print('\b' * len(positionText), end='', flush=True)
            sleep(POLL_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print('\n')


if __name__ == '__main__':
    import pyautogui
    pyautogui.PAUSE = 0.5
    pyautogui.FAILSAFE = True

    trackMouse()
