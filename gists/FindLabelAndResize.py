#!/usr/bin/env python
# /// script
# dependencies = ['pillow', 'pyautogui', 'opencv-python', 'codeallybasic', 'pyobjc-framework-Quartz']
# ///
from typing import Callable

import pyautogui

from pyautogui import click
from pyautogui import drag
from pyautogui import moveTo

from umldiagrammeruitests.Common import makeAppActive
from umldiagrammeruitests.locators.BaseLocator import BoundingBox
from umldiagrammeruitests.locators.BaseLocator import Location
from umldiagrammeruitests.locators.LinkDialogLocator import LinkDialogLocator

def selectAndResizeLabel(
    labelLocation:     Location,
    selectedBoxGetter: Callable[[], BoundingBox],
    dragDeltaX:        int
):
    """

    Args:
        labelLocation:          The plain label location
        selectedBoxGetter:      The appropriate property
        dragDeltaX:             How much to resize it

    """
    click(x=labelLocation.x, y=labelLocation.y)

    selectedBoundingBox: BoundingBox = selectedBoxGetter()
    sizerLocation:       Location    = rightSizerLocation(boundingBox=selectedBoundingBox)

    resizeLabelByOffset(sizerLocation=sizerLocation, dragDeltaX=dragDeltaX)

def resizeLabelByOffset(sizerLocation: Location, dragDeltaX: int):
    """

    Args:
        sizerLocation:  The specific location of the sizer, doohickey
        dragDeltaX:     How much to increase the size

    """
    # 1. Move to the middle-right sizer
    moveTo(x=sizerLocation.x, y=sizerLocation.y, duration=0.5)

    # 2. Click and drag horizontally to the right
    drag(xOffset=dragDeltaX, yOffset=0, duration=0.8, button='left')

def rightSizerLocation(boundingBox: BoundingBox) -> Location:
    """
    Assumes a 'tight' image
    Args:
        boundingBox: The bounding box that encompasses the selected label

    """

    rightSizerX: int = boundingBox.left + boundingBox.width
    rightSizerY: int = boundingBox.top + (boundingBox.height // 2)

    sizerLocation: Location = Location(x=rightSizerX, y=rightSizerY)

    return sizerLocation


pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

makeAppActive()

linkDialogLocator: LinkDialogLocator = LinkDialogLocator()


selectAndResizeLabel(
    labelLocation=linkDialogLocator.associationNameLabel,
    selectedBoxGetter=lambda: linkDialogLocator.associationNameLabelSelected,
    dragDeltaX=60
)

selectAndResizeLabel(
    labelLocation=linkDialogLocator.destinationCardinalityLabel,
    selectedBoxGetter=lambda: linkDialogLocator.destinationCardinalityLabelSelected,
    dragDeltaX=100
)

selectAndResizeLabel(
    labelLocation=linkDialogLocator.sourceCardinalityLabel,
    selectedBoxGetter=lambda: linkDialogLocator.sourceCardinalityLabelSelected,
    dragDeltaX=70
)
