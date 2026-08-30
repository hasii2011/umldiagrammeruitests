#!/usr/bin/env python
# /// script
# dependencies = ['pillow', 'pyautogui', 'codeallybasic', 'opencv-python', 'pyobjc-framework-Quartz']
# ///

from time import sleep as pySleep

from subprocess import run as subProcessRun

from pyautogui import moveTo
from pyautogui import click
from pyautogui import press
from pyautogui import hotkey

from click import secho

from umldiagrammeruitests.Common import APPLE_SCRIPT_SEND_KEYSTROKES
from umldiagrammeruitests.Common import makeAppActive

from umldiagrammeruitests.MacOsDoubleClickHandler import MacOsDoubleClickHandler
from umldiagrammeruitests.locators.BaseLocator import Location
from umldiagrammeruitests.locators.CommonImageLocator import CommonImageLocator

import pyautogui

from umldiagrammeruitests.locators.LinkDialogLocator import LinkDialogLocator

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

def changeLinkAttribute(attributeLocation: Location, oldName: str, newName: str):

    click(x=attributeLocation.x, y=attributeLocation.y)
    hotkey('command', 'right')
    press('backspace', len(oldName))
    # typewrite(message=newName, interval=TYPE_WRITE_INTERVAL)
    applescript: str = f'{APPLE_SCRIPT_SEND_KEYSTROKES} "{newName}"'
    subProcessRun(['osascript', '-e', applescript])


makeAppActive()

locator: CommonImageLocator = CommonImageLocator()
location: Location = locator.clickToOpenAssociationDialog
secho(f'{location=}')

doubleClickLocation: Location = Location(x=location.x + 1, y=location.y + 10)
secho(f'{doubleClickLocation=}')

moveTo(x=doubleClickLocation.x, y=doubleClickLocation.y, duration=1.0)
MacOsDoubleClickHandler.doubleClick(x=doubleClickLocation.x, y=doubleClickLocation.y)

linkDialogLocator: LinkDialogLocator = LinkDialogLocator()

pySleep(1.0)    # Wait for the dialog to appear

srcCardLocation: Location = linkDialogLocator.sourceCardinalityTextInput
changeLinkAttribute(attributeLocation=srcCardLocation, oldName='src Card', newName='SourceCardinality')

associationNameLocation: Location = linkDialogLocator.associationNameTextInput

changeLinkAttribute(attributeLocation=associationNameLocation, oldName='Association-0', newName='TestAssociation')

dstCardLocation: Location = linkDialogLocator.destinationCardinalityTextInput
changeLinkAttribute(attributeLocation=dstCardLocation, oldName='dst Card', newName='DestinationCardinality')
