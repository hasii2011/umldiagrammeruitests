
from typing import Callable

from logging import Logger
from logging import getLogger

from time import sleep as pySleep

from pathlib import Path

from click import secho

from pyautogui import click
from pyautogui import drag
from pyautogui import hotkey
from pyautogui import moveTo
from pyautogui import press

from umldiagrammeruitests.MacOsDoubleClickHandler import MacOsDoubleClickHandler
from umldiagrammeruitests.MacOsTypeWriteHandler import MacOsTypeWriteHandler

from umldiagrammeruitests.locators.BaseLocator import Location
from umldiagrammeruitests.locators.BaseLocator import BoundingBox
from umldiagrammeruitests.locators.LinkDialogLocator import LinkDialogLocator

from umldiagrammeruitests.verifiers.AggregationCreator import AggregationCreator

BASENAME:                               str  = 'AssociationLabelTest'
ASSOCIATION_LABEL_XML_FILENAME:         str = f'{BASENAME}.xml'
ASSOCIATION_LABEL_PROJECT_FILENAME:     Path = Path(f'/tmp/{BASENAME}.udt')
DECOMPRESSED_ASSOCIATION_LABEL_PROJECT: Path = Path(f'/tmp/{ASSOCIATION_LABEL_XML_FILENAME}')


class AssociationLabelVerifier(AggregationCreator):

    def __init__(self):
        super().__init__(aggregationProjectFileName=ASSOCIATION_LABEL_PROJECT_FILENAME, decompressedAggregationFileName=DECOMPRESSED_ASSOCIATION_LABEL_PROJECT)

        self._macOsTypeWriteHandler: MacOsTypeWriteHandler = MacOsTypeWriteHandler()
        self._linkDialogLocator:     LinkDialogLocator     = LinkDialogLocator()

        self.logger: Logger = getLogger(__name__)

    def execute(self):
        """
        Use the common code to create an aggregation diagram.
        Then it
            * Changes the names of the association name and cardinalities
            * Resizes the label to make them look better

        This should create a unique project and we will verify it so
        """

        super().execute()

        self._bringUmlDiagrammerToForeground()

        self._createAggregationDiagram()

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

        self._selectAndResizeLabel(
            labelLocation=self._linkDialogLocator.associationNameLabel,
            selectedBoxGetter=lambda: self._linkDialogLocator.associationNameLabelSelected,
            dragDeltaX=60
        )

        self._selectAndResizeLabel(
            labelLocation=self._linkDialogLocator.destinationCardinalityLabel,
            selectedBoxGetter=lambda: self._linkDialogLocator.destinationCardinalityLabelSelected,
            dragDeltaX=100
        )

        self._selectAndResizeLabel(
            labelLocation=self._linkDialogLocator.sourceCardinalityLabel,
            selectedBoxGetter=lambda: self._linkDialogLocator.sourceCardinalityLabelSelected,
            dragDeltaX=70
        )
        #
        # All we have to do is click the save button again.  _createAggregationDiagram did
        # the initial save
        #
        self._saveAsProject.pressSaveProject()

    def _changeLinkAttribute(self, attributeLocation: Location, oldName: str, newName: str):

        click(x=attributeLocation.x, y=attributeLocation.y)
        hotkey('command', 'right')
        press('backspace', len(oldName))

        self._macOsTypeWriteHandler.typeWrite(textToWrite=newName)

    def _selectAndResizeLabel(self,
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
        sizerLocation: Location = self._rightSizerLocation(boundingBox=selectedBoundingBox)

        self._resizeLabelByOffset(sizerLocation=sizerLocation, dragDeltaX=dragDeltaX)

    def _rightSizerLocation(self, boundingBox: BoundingBox) -> Location:
        """
        Assumes a 'tight' image
        Args:
            boundingBox: The bounding box that encompasses the selected label

        """
        rightSizerX: int = boundingBox.left + boundingBox.width
        rightSizerY: int = boundingBox.top + (boundingBox.height // 2)

        sizerLocation: Location = Location(x=rightSizerX, y=rightSizerY)

        return sizerLocation

    def _resizeLabelByOffset(self, sizerLocation: Location, dragDeltaX: int):
        """

        Args:
            sizerLocation:  The specific location of the sizer, doohickey
            dragDeltaX:     How much to increase the size

        """
        # 1. Move to the middle-right sizer
        moveTo(x=sizerLocation.x, y=sizerLocation.y, duration=0.5)

        # 2. Click and drag horizontally to the right
        drag(xOffset=dragDeltaX, yOffset=0, duration=0.8, button='left')
