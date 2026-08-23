
from logging import Logger
from logging import getLogger

from os import sep as osSep

from pathlib import Path

from pyautogui import click
from pyautogui import typewrite

from umldiagrammeruitests.locators.BaseLocator import Location
from umldiagrammeruitests.verifiers.BaseVerifier import BaseVerifier

WELL_KNOWN_CLASS_NAME: str = 'ClassWithVariousOptionsChanged'

#
# Removed the IDs
#
GOLDEN_CLASS_XML: str = (
    "<?xml version='1.0' encoding='iso-8859-1'?>\n"
    '<UmlProject fileName="/private/tmp/ClassOptionsTest.udt" version="14.0" codePath=".">\n'
    '    <UMLDiagram documentType="Class Document" title="Class Diagram" scrollPositionX="0" scrollPositionY="0" pixelsPerUnitX="20" pixelsPerUnitY="20">\n'
    '        <UmlClass id="" width="258" height="90" x="224" y="267">\n'
    '            <ModelClass id="" name="ClassWithVariousOptionsChanged" stereotype="thread" displayMethods="False" displayParameters="Unspecified" displayConstructor="Unspecified" displayDunderMethods="Unspecified" displayFields="False" displayStereotype="False" fileName="" description="I am supposed to describe this class" />\n'
    '        </UmlClass>\n'
    '    </UMLDiagram>\n'
    '</UmlProject>'
)

BASENAME:                    str = 'ClassOptionsTest'
CLASS_OPTIONS_XML_FILENAME:  str = f'{BASENAME}.xml'

CLASS_OPTIONS_PROJECT_FILENAME:     Path = Path(f'{osSep}tmp{osSep}{BASENAME}.udt')
DECOMPRESSED_CLASS_OPTIONS_PROJECT: Path = Path(f'{osSep}tmp{osSep}{CLASS_OPTIONS_XML_FILENAME}')

LOC_WHERE_CLASS_IS_CREATED: Location = Location(x=500, y=370)


class ClassOptionsVerifier(BaseVerifier):

    def __init__(self):
        super().__init__()
        self.logger: Logger = getLogger(__name__)

    def execute(self):

        super().execute()

        CLASS_OPTIONS_PROJECT_FILENAME.unlink(missing_ok=True)
        DECOMPRESSED_CLASS_OPTIONS_PROJECT.unlink(missing_ok=True)

        self._bringUmlDiagrammerToForeground()

        self._toolBarClicker.clickNewClass()

        click(x=LOC_WHERE_CLASS_IS_CREATED.x, y=LOC_WHERE_CLASS_IS_CREATED.y)

        self._renameUmlClass(newClassName=WELL_KNOWN_CLASS_NAME)

        #
        # These methods assume that the default is 'On'
        #
        self._turnOffShowStereoType()
        self._turnOffShowFields()
        self._turnOffShowMethods()
        self._setADescription()
        self._setStereotype()
        #
        # Ok, I am done with the customizations
        #
        clickClassOkButton: Location = self._classDialogLocator.clickClassOkButton
        click(x=clickClassOkButton.x, y=clickClassOkButton.y)

        self._saveAsProject.execute(projectFileName=str(CLASS_OPTIONS_PROJECT_FILENAME))

        self._verifyTest(
            projectFileName=CLASS_OPTIONS_PROJECT_FILENAME,
            decompressedProjectFileName=DECOMPRESSED_CLASS_OPTIONS_PROJECT,
            goldenXml=GOLDEN_CLASS_XML
        )

    def _turnOffShowStereoType(self):
        location: Location = self._classDialogLocator.showStereotypeCheckBox
        click(x=location.x, y=location.y)

    def _turnOffShowFields(self):
        location: Location = self._classDialogLocator.showFieldsCheckBox
        click(x=location.x, y=location.y)

    def _turnOffShowMethods(self):
        location: Location = self._classDialogLocator.showMethodsCheckBox
        click(x=location.x, y=location.y)

    def _setADescription(self):

        location: Location = self._classDialogLocator.descriptionButton
        click(x=location.x, y=location.y)

        descriptionTextLocation: Location = self._classDialogLocator.descriptionTextBox
        click(x=descriptionTextLocation.x, y=descriptionTextLocation.y)

        typewrite('I am supposed to describe this class')

        descriptionOkButtonLocation: Location = self._classDialogLocator.descriptionOkButton
        click(x=descriptionOkButtonLocation.x, y=descriptionOkButtonLocation.y)

    def _setStereotype(self):

        location: Location = self._classDialogLocator.stereoTypeButton
        click(x=location.x, y=location.y)

        threadSelectionLocation: Location = self._classDialogLocator.threadStereoTypeSelection
        click(x=threadSelectionLocation.x, y=threadSelectionLocation.y)

        stereotypeOkButtonLocation: Location = self._classDialogLocator.stereotypeOkButton
        click(x=stereotypeOkButtonLocation.x, y=stereotypeOkButtonLocation.y)
