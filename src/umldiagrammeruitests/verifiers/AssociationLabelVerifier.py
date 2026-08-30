
from logging import Logger
from logging import getLogger

from time import sleep as pySleep

from pathlib import Path

from click import secho

from pyautogui import click
from pyautogui import hotkey
from pyautogui import press

from umldiagrammeruitests.MacOsDoubleClickHandler import MacOsDoubleClickHandler
from umldiagrammeruitests.MacOsTypeWriteHandler import MacOsTypeWriteHandler
from umldiagrammeruitests.locators.BaseLocator import Location
from umldiagrammeruitests.locators.LinkDialogLocator import LinkDialogLocator
from umldiagrammeruitests.verifiers.AggregationCreator import AggregationCreator

BASENAME:                         str  = 'AssociationLabelTest'
AGGREGATION_XML_FILENAME:         str = f'{BASENAME}.xml'
AGGREGATION_PROJECT_FILENAME:     Path = Path(f'/tmp/{BASENAME}.udt')
DECOMPRESSED_AGGREGATION_PROJECT: Path = Path(f'/tmp/{AGGREGATION_XML_FILENAME}')


class AssociationLabelVerifier(AggregationCreator):

    def __init__(self):
        super().__init__(aggregationProjectFileName=AGGREGATION_PROJECT_FILENAME, decompressedAggregationFileName=DECOMPRESSED_AGGREGATION_PROJECT)

        self._macOsTypeWriteHandler: MacOsTypeWriteHandler = MacOsTypeWriteHandler()
        self._linkDialogLocator:     LinkDialogLocator     = LinkDialogLocator()

        self.logger: Logger = getLogger(__name__)

    def execute(self):

        super().execute()

        self._bringUmlDiagrammerToForeground()

        self._createAggregationDiagram()

        # sourceCardinalityLocation: Location = self._commonImageLocator.sourceCardinality
        # secho(f'{sourceCardinalityLocation=}')

        # destinationCardinalityLocation: Location = self._commonImageLocator.destinationCardinality
        # secho(f'{destinationCardinalityLocation=}')

        associationLabelCardinalityLocation: Location = self._commonImageLocator.associationLabel
        secho(f'{associationLabelCardinalityLocation=}')

        doubleClickX: int = associationLabelCardinalityLocation.x + 7
        doubleClickY: int = associationLabelCardinalityLocation.y + 25

        secho(f'Double click at: ({doubleClickX},{doubleClickY})')
        MacOsDoubleClickHandler.doubleClick(x=doubleClickX, y=doubleClickY)

        pySleep(1.0)  # Wait for the dialog to appear

        srcCardLocation: Location = self._linkDialogLocator.sourceCardinalityTextInput
        self._changeLinkAttribute(attributeLocation=srcCardLocation, oldName='src Card', newName='SourceCardinality')

        associationNameLocation: Location = self._linkDialogLocator.associationNameTextInput

        self._changeLinkAttribute(attributeLocation=associationNameLocation, oldName='Association-0', newName='TestAssociation')

        dstCardLocation: Location = self._linkDialogLocator.destinationCardinalityTextInput
        self._changeLinkAttribute(attributeLocation=dstCardLocation, oldName='dst Card', newName='DestinationCardinality')

        okButtonLocation: Location = self._linkDialogLocator.okButton
        click(okButtonLocation.x, okButtonLocation.y)


    def _changeLinkAttribute(self, attributeLocation: Location, oldName: str, newName: str):

        click(x=attributeLocation.x, y=attributeLocation.y)
        hotkey('command', 'right')
        press('backspace', len(oldName))
        # typewrite(message=newName, interval=TYPE_WRITE_INTERVAL)
        # applescript: str = f'{APPLE_SCRIPT_SEND_KEYSTROKES} "{newName}"'
        # subProcessRun(['osascript', '-e', applescript])

        self._macOsTypeWriteHandler.typeWrite(textToWrite=newName)
