#!/usr/bin/env python
# /// script
# dependencies = ['pyautogui', 'pillow']
# ///
from PIL.Image import Image

from pyautogui import screenshot

if __name__ == '__main__':

    img: Image = screenshot('my_screenshot.png')

    img.save('screenshot.png')

    print(f'{img=}')    # noqa
    print(f'{img.size=}, {img.mode=}')  # noqa
