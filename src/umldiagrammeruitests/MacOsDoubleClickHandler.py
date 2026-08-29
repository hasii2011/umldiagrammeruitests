
from logging import Logger
from logging import getLogger

from Quartz.CoreGraphics import CGEventPost                     # noqa
from Quartz.CoreGraphics import kCGHIDEventTap                  # noqa
from Quartz.CoreGraphics import kCGMouseButtonLeft              # noqa
from Quartz.CoreGraphics import kCGEventLeftMouseUp             # noqa
from Quartz.CoreGraphics import kCGEventLeftMouseDown           # noqa
from Quartz.CoreGraphics import CGEventCreateMouseEvent         # noqa
from Quartz.CoreGraphics import kCGMouseEventClickState         # noqa
from Quartz.CoreGraphics import CGEventSetIntegerValueField     # noqa
from Quartz.CoreGraphics import CGEventRef                      # noqa


class MacOsDoubleClickHandler:
    """
    This code resides here to compartmentalize the necessary imports
    """

    def __init__(self):
        self.logger: Logger = getLogger(__name__)

    @classmethod
    def doubleClick(cls, x: int, y: int):
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

        firstMouseDown: CGEventRef = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, clickLocation, kCGMouseButtonLeft)
        CGEventSetIntegerValueField(firstMouseDown, kCGMouseEventClickState, 1)

        firstMouseUp: CGEventRef = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, clickLocation, kCGMouseButtonLeft)
        CGEventSetIntegerValueField(firstMouseUp, kCGMouseEventClickState, 1)

        secondMouseDown: CGEventRef = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, clickLocation, kCGMouseButtonLeft)
        CGEventSetIntegerValueField(secondMouseDown, kCGMouseEventClickState, 2)

        secondMouseUp: CGEventRef = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, clickLocation, kCGMouseButtonLeft)
        CGEventSetIntegerValueField(secondMouseUp, kCGMouseEventClickState, 2)

        CGEventPost(kCGHIDEventTap, firstMouseDown)
        CGEventPost(kCGHIDEventTap, firstMouseUp)
        CGEventPost(kCGHIDEventTap, secondMouseDown)
        CGEventPost(kCGHIDEventTap, secondMouseUp)
