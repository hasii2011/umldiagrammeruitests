#!/usr/bin/env python
# /// script
# dependencies = ['pillow', 'pyautogui', 'umlshapes', 'opencv-python', 'pyobjc-framework-Quartz']
# ///
from click import secho
from pyautogui import moveTo

# noinspection PyUnresolvedReferences
from Quartz.CoreGraphics import CGEventCreateMouseEvent
# noinspection PyUnresolvedReferences
from Quartz.CoreGraphics import CGEventPost
# noinspection PyUnresolvedReferences
from Quartz.CoreGraphics import CGEventSetIntegerValueField
# noinspection PyUnresolvedReferences
from Quartz.CoreGraphics import kCGEventLeftMouseDown
# noinspection PyUnresolvedReferences
from Quartz.CoreGraphics import kCGEventLeftMouseUp
# noinspection PyUnresolvedReferences
from Quartz.CoreGraphics import kCGHIDEventTap
# noinspection PyUnresolvedReferences
from Quartz.CoreGraphics import kCGMouseButtonLeft
# noinspection PyUnresolvedReferences
from Quartz.CoreGraphics import kCGMouseEventClickState

from umldiagrammeruitests.Common import makeAppActive
from umldiagrammeruitests.locators.BaseLocator import Location
from umldiagrammeruitests.locators.CommonImageLocator import CommonImageLocator

import pyautogui


def macOsDoubleClick(x: int, y: int) -> None:
    """
    Dispatches a native macOS double-click event via Quartz Event Services.

    Rationale:
        UML Diagrammer is built on wxWidgets / wxPython, which on macOS Cocoa
        relies directly on [NSEvent clickCount] == 2 to generate wxEVT_LEFT_DCLICK.

        PyAutoGUI's built-in doubleClick() on macOS creates two generic CGEvent
        instances without incrementing kCGMouseEventClickState to 2. Consequently,
        Cocoa sees both events as clickCount = 1 (two separate single clicks), which
        selects or toggles the element (turning it red) but never triggers the
        dialog-opening double-click event.

        This function explicitly sets kCGMouseEventClickState to 1 for the first
        mouse-down/up pair and 2 for the second pair, ensuring macOS Cocoa and
        wxWidgets properly register the gesture as a true double click.

    Args:
        x: Logical X coordinate on screen.
        y: Logical Y coordinate on screen.
    """
    clickLocation: tuple[int, int] = (x, y)

    firstMouseDown = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, clickLocation, kCGMouseButtonLeft)
    CGEventSetIntegerValueField(firstMouseDown, kCGMouseEventClickState, 1)

    firstMouseUp = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, clickLocation, kCGMouseButtonLeft)
    CGEventSetIntegerValueField(firstMouseUp, kCGMouseEventClickState, 1)

    secondMouseDown = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, clickLocation, kCGMouseButtonLeft)
    CGEventSetIntegerValueField(secondMouseDown, kCGMouseEventClickState, 2)

    secondMouseUp = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, clickLocation, kCGMouseButtonLeft)
    CGEventSetIntegerValueField(secondMouseUp, kCGMouseEventClickState, 2)

    CGEventPost(kCGHIDEventTap, firstMouseDown)
    CGEventPost(kCGHIDEventTap, firstMouseUp)
    CGEventPost(kCGHIDEventTap, secondMouseDown)
    CGEventPost(kCGHIDEventTap, secondMouseUp)


pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

makeAppActive()

locator: CommonImageLocator = CommonImageLocator()
location: Location = locator.clickToOpenAssociationDialog
secho(f'{location=}')

doubleClickLocation: Location = Location(x=location.x + 1, y=location.y + 10)
secho(f'{doubleClickLocation=}')

moveTo(x=doubleClickLocation.x, y=doubleClickLocation.y, duration=1.0)
macOsDoubleClick(x=doubleClickLocation.x, y=doubleClickLocation.y)
