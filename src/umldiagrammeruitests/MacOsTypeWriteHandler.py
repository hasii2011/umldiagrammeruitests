
from logging import Logger
from logging import getLogger

from time import sleep as pySleep

from subprocess import run as subProcessRun

APPLE_SCRIPT_SEND_KEYSTROKES: str   = 'tell application "System Events" to keystroke'
POST_APPLE_SCRIPT_DELAY:      float = 0.3


class MacOsTypeWriteHandler:
    """
    Handles reliable text entry on macOS by routing keystrokes through AppleScript System Events.

    Rationale:
        PyAutoGUI's built-in typewrite() simulates text entry by converting characters into raw
        hardware virtual keycodes and rapidly toggling synthetic Shift modifier keys for uppercase
        letters and special symbols (e.g. '/', '.', '_', ':').

        On macOS, this approach exhibits known reliability issues:

        1. Modifier Desynchronization: Synthetic Shift keyUp events are frequently dropped by the
           macOS WindowServer, leaving the Shift key stuck in a 'down' state and corrupting subsequent
           keystrokes and shortcuts.
        2. Dropped Punctuation: Rapid Shift down/up cycling often causes special characters (such as
           slashes and dots in file paths) to be skipped or misordered.
        3. Native Cocoa Dialogs: Modal sheets and file dialogs listen to high-level NSTextInputClient
           events rather than low-level scan codes, causing raw synthetic keycodes to be ignored.

        By dispatching text via AppleScript (APPLE_SCRIPT_SEND_KEYSTROKES), text
        is injected directly as high-level Unicode input into the active text field, avoiding
        synthetic modifier state bugs and guaranteeing accurate path and text entry.
    """

    def __init__(self):
        self.logger: Logger = getLogger(__name__)

    @classmethod
    def typeWrite(cls, textToWrite: str):
        """
        Uses native macOS AppleScript to send keystrokes directly to the dialog,
        bypassing PyAutoGUI character encoding limitations.

        Args:
            textToWrite: The text string to send to the active input field
        """
        applescript: str = f'{APPLE_SCRIPT_SEND_KEYSTROKES} "{textToWrite}"'

        subProcessRun(['osascript', '-e', applescript])

        pySleep(POST_APPLE_SCRIPT_DELAY)
