#!/usr/bin/env python
# /// script
# dependencies = ['pillow', 'pyautogui', 'umlshapes', 'opencv-python']
# ///
from typing import Any
from typing import Dict

from logging import debug
from logging import error
from logging import info

from pyautogui import size
from pyautogui import ImageNotFoundException

from umldiagrammeruitests.locators.BaseLocator import Location
from umldiagrammeruitests.locators.ToolBarIconLocator import ToolBarIconLocator
from umldiagrammeruitests.Common import setupLogging

if __name__ == '__main__':
    setupLogging()
    info('Remember.  The image size has to match')
    info(f'Screen size{size()}')

    iconProperties: Dict[str, property] = {}
    for attributeName in dir(ToolBarIconLocator):
        potentialProperty: Any = getattr(ToolBarIconLocator, attributeName)
        if isinstance(potentialProperty, property):
            iconProperties[attributeName] = potentialProperty

    debug(f'The icon properties are: {iconProperties}')

    iconLocator: ToolBarIconLocator = ToolBarIconLocator()
    for propName in iconProperties.keys():
        try:
            targetLocation: Location = getattr(iconLocator, propName)
            info(f'{propName} - ({targetLocation.x},{targetLocation.y})')
        except ImageNotFoundException:
            error(f'Where the heck is the image for {propName}')
