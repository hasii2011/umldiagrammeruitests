#!/usr/bin/env python
# /// script
# dependencies = ['pillow', 'pyautogui', 'opencv-python', 'codeallybasic', 'pyobjc-framework-Quartz']
# ///

import pyautogui

from pyautogui import click
from pyautogui import drag
from pyautogui import moveTo

from umldiagrammeruitests.Common import makeAppActive
from umldiagrammeruitests.locators.BaseLocator import BoundingBox
from umldiagrammeruitests.locators.BaseLocator import Location
from umldiagrammeruitests.locators.LinkDialogLocator import LinkDialogLocator


def resizeLabelByOffset(sizerLocation: Location, dragDeltaX: int):
    # 1. Move to the middle-right sizer
    moveTo(x=sizerLocation.x, y=sizerLocation.y, duration=0.5)

    # 2. Click and drag horizontally to the right
    drag(xOffset=dragDeltaX, yOffset=0, duration=0.8, button='left')

def rightSizerLocation(boundingBox: BoundingBox) -> Location:

    rightSizerX: int = boundingBox.left + boundingBox.width
    rightSizerY: int = boundingBox.top + (boundingBox.height // 2)

    sizerLocation: Location = Location(x=rightSizerX, y=rightSizerY)

    return sizerLocation


pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

makeAppActive()

linkDialogLocator: LinkDialogLocator = LinkDialogLocator()


associationNameLabelLocation: Location = linkDialogLocator.associationNameLabel
click(x=associationNameLabelLocation.x, y=associationNameLabelLocation.y)

associationNameBoundingBox:  BoundingBox = linkDialogLocator.associationNameLabelSelected
associationNameSizeLocation: Location    = rightSizerLocation(boundingBox=associationNameBoundingBox)
resizeLabelByOffset(sizerLocation=associationNameSizeLocation, dragDeltaX=60)

destinationCardinalityLocation: Location = linkDialogLocator.destinationCardinalityLabel
click(x=destinationCardinalityLocation.x, y=destinationCardinalityLocation.y)

destinationCardinalityBox: BoundingBox = linkDialogLocator.destinationCardinalityLabelSelected
destinationSizerLocation:  Location    = rightSizerLocation(boundingBox=destinationCardinalityBox)
resizeLabelByOffset(sizerLocation=destinationSizerLocation, dragDeltaX=100)


sourceCardinalityLocation: Location = linkDialogLocator.sourceCardinalityLabel
click(x=sourceCardinalityLocation.x, y=sourceCardinalityLocation.y)

sourceCardinalityBoundingBox: BoundingBox = linkDialogLocator.sourceCardinalityLabelSelected
sourceSizerLocation:          Location    = rightSizerLocation(boundingBox=sourceCardinalityBoundingBox)
resizeLabelByOffset(sizerLocation=sourceSizerLocation, dragDeltaX=70)
