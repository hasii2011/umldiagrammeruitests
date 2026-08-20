from logging import Logger
from logging import getLogger
from pathlib import Path

from pyautogui import click
from pyautogui import press
from pyautogui import typewrite

from umldiagrammeruitests.Common import TYPE_WRITE_INTERVAL
from umldiagrammeruitests.locators.BaseLocator import Location
from umldiagrammeruitests.verifiers.BaseVerifier import BaseVerifier

#
# Removed the IDs
#
GOLDEN_NOTE_LINK_XML: str = (
    "<?xml version='1.0' encoding='iso-8859-1'?>\n"
    '<UmlProject fileName="/private/tmp/notelinktest.udt" version="14.0" codePath=".">\n'
    '    <UMLDiagram documentType="Class Document" title="Class Diagram" scrollPositionX="0" scrollPositionY="0" pixelsPerUnitX="20" pixelsPerUnitY="20">\n'
    '        <UmlClass id="" width="112" height="90" x="224" y="97">\n'
    '            <ModelClass id="" name="ClassWithNote" displayMethods="True" displayParameters="Unspecified" displayConstructor="Unspecified" displayDunderMethods="Unspecified" displayFields="True" displayStereotype="True" fileName="" description="" />\n'
    '        </UmlClass>\n'
    '        <UmlNote id="" width="150" height="50" x="449" y="547">\n'
    '            <ModelNote id="" content="I am a UI test note" fileName="" />\n'
    '        </UmlNote>\n'
    '        <UmlLink id="" fromX="510" fromY="547" toX="306" toY="187" spline="False">\n'
    '            <ModelLink name="" type="NOTELINK" sourceId="" destinationId="" bidirectional="False" sourceCardinalityValue="" destinationCardinalityValue="" />\n'
    '        </UmlLink>\n'
    '    </UMLDiagram>\n'
    '</UmlProject>'
)

WELL_KNOWN_CLASS_NAME: str = 'ClassWithNote'

BASENAME:                         str  = 'notelinktest'
NOTE_LINK_XML_FILENAME:           str = f'{BASENAME}.xml'

NOTE_LINK_PROJECT_FILENAME:       Path = Path(f'/tmp/{BASENAME}.udt')
DECOMPRESSED_NOTE_PROJECT: Path = Path(f'/tmp/{NOTE_LINK_XML_FILENAME}')

LOC_WHERE_CLASS_IS_CREATED: Location = Location(x=500, y=200)
LOC_WHERE_NOTE_IS_CREATED:  Location = Location(x=725, y=650)

class NoteLinkVerifier(BaseVerifier):

    def __init__(self):
        super().__init__()
        self.logger: Logger = getLogger(__name__)

    def execute(self):
        super().execute()

        NOTE_LINK_PROJECT_FILENAME.unlink(missing_ok=True)
        DECOMPRESSED_NOTE_PROJECT.unlink(missing_ok=True)

        self._bringUmlDiagrammerToForeground()

        self._toolBarClicker.clickNewClass()

        click(x=LOC_WHERE_CLASS_IS_CREATED.x, y=LOC_WHERE_CLASS_IS_CREATED.y)

        self._renameUmlClass(newClassName=WELL_KNOWN_CLASS_NAME)

        clickClassOkButton: Location = self._classDialogLocator.clickClassOkButton
        click(x=clickClassOkButton.x, y=clickClassOkButton.y)

        self._toolBarClicker.clickNewNote()

        click(x=LOC_WHERE_NOTE_IS_CREATED.x, y=LOC_WHERE_NOTE_IS_CREATED.y)

        noteTextLocation: Location = self._commonImageLocator.defaultNoteText
        click(x=noteTextLocation.x, y=noteTextLocation.y)
        press('backspace', presses=len('This is the note text'))
        typewrite('I am a UI test note', interval=TYPE_WRITE_INTERVAL)

        noteOkButtonLocation: Location = self._commonImageLocator.okButton
        click(x=noteOkButtonLocation.x, y=noteOkButtonLocation.y)

        self._toolBarClicker.clickNoteLink()

        noteLocation: Location = self._commonImageLocator.uiTestNote
        click(x=noteLocation.x, y=noteLocation.y)

        classWithNoteLocation: Location = self._commonImageLocator.classWithNote
        click(x=classWithNoteLocation.x, y=classWithNoteLocation.y)

        self._saveAsProject.execute(projectFileName=str(NOTE_LINK_PROJECT_FILENAME))

        self._verifyTest(
            projectFileName=NOTE_LINK_PROJECT_FILENAME,
            decompressedProjectFileName=DECOMPRESSED_NOTE_PROJECT,
            goldenXml=GOLDEN_NOTE_LINK_XML
        )
