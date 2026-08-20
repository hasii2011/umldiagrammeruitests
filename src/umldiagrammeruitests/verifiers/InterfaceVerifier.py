
from logging import Logger
from logging import getLogger

from pathlib import Path

from pyautogui import click

from umldiagrammeruitests.locators.BaseLocator import Location
from umldiagrammeruitests.verifiers.BaseVerifier import BaseVerifier

#
# Removed the IDs
# Note even though interface always generate 'implements' as a name
# It is removed by the verifier;  So I cannot test for it;
#
GOLDEN_INTERFACE_LINK_XML: str = (
    "<?xml version='1.0' encoding='iso-8859-1'?>\n"
    '<UmlProject fileName="/private/tmp/interfacelinktest.udt" version="14.0" codePath=".">\n'
    '    <UMLDiagram documentType="Class Document" title="Class Diagram" scrollPositionX="0" scrollPositionY="0" pixelsPerUnitX="20" pixelsPerUnitY="20">\n'
    '        <UmlClass id="" width="71" height="90" x="224" y="97">\n'
    '            <ModelClass id="" name="IInterface" displayMethods="True" displayParameters="Unspecified" displayConstructor="Unspecified" displayDunderMethods="Unspecified" displayFields="True" displayStereotype="True" fileName="" description="" />\n'
    '        </UmlClass>\n'
    '        <UmlClass id="" width="94" height="90" x="449" y="247">\n'
    '            <ModelClass id="" name="Implementor" displayMethods="True" displayParameters="Unspecified" displayConstructor="Unspecified" displayDunderMethods="Unspecified" displayFields="True" displayStereotype="True" fileName="" description="" />\n'
    '        </UmlClass>\n'
    '        <UmlLink id="" fromX="449" fromY="262" toX="294" toY="164" spline="False">\n'
    '            <ModelLink name="" type="INTERFACE" sourceId="" destinationId="" bidirectional="False" sourceCardinalityValue="" destinationCardinalityValue="" />\n'
    '        </UmlLink>\n'
    '    </UMLDiagram>\n'
    '</UmlProject>'
)

BASENAME:               str  = 'interfacelinktest'
INTERFACE_XML_FILENAME: str = f'{BASENAME}.xml'

INTERFACE_PROJECT_FILENAME:     Path = Path(f'/tmp/{BASENAME}.udt')
DECOMPRESSED_INTERFACE_PROJECT: Path = Path(f'/tmp/{INTERFACE_XML_FILENAME}')

LOC_WHERE_INTERFACE_IS_CREATED:   Location = Location(x=500, y=200)
LOC_WHERE_IMPLEMENTOR_IS_CREATED: Location = Location(x=725, y=350)

INTERFACE_CLASS_NAME:   str = 'IInterface'
IMPLEMENTOR_CLASS_NAME: str = 'Implementor'

class InterfaceVerifier(BaseVerifier):
    def __init__(self):
        super().__init__()
        self.logger: Logger = getLogger(__name__)

    def execute(self):
        super().execute()

        INTERFACE_PROJECT_FILENAME.unlink(missing_ok=True)
        DECOMPRESSED_INTERFACE_PROJECT.unlink(missing_ok=True)

        self._bringUmlDiagrammerToForeground()

        self._toolBarClicker.clickNewClass()

        click(x=LOC_WHERE_INTERFACE_IS_CREATED.x, y=LOC_WHERE_INTERFACE_IS_CREATED.y)

        self._renameUmlClass(newClassName=INTERFACE_CLASS_NAME)

        clickClassOkButton: Location = self._classDialogLocator.clickClassOkButton
        click(x=clickClassOkButton.x, y=clickClassOkButton.y)

        self._toolBarClicker.clickNewClass()
        click(x=LOC_WHERE_IMPLEMENTOR_IS_CREATED.x, y=LOC_WHERE_IMPLEMENTOR_IS_CREATED.y)
        self._renameUmlClass(newClassName=IMPLEMENTOR_CLASS_NAME)
        click(x=clickClassOkButton.x, y=clickClassOkButton.y)

        self._toolBarClicker.clickInterface()

        implementorLocation: Location = self._commonImageLocator.implementorClass
        click(x=implementorLocation.x, y=implementorLocation.y)

        interfaceLocation: Location = self._commonImageLocator.interfaceClass
        click(x=interfaceLocation.x, y=interfaceLocation.y)

        self._saveAsProject.execute(projectFileName=str(INTERFACE_PROJECT_FILENAME))

        self._verifyTest(
            projectFileName=INTERFACE_PROJECT_FILENAME,
            decompressedProjectFileName=DECOMPRESSED_INTERFACE_PROJECT,
            goldenXml=GOLDEN_INTERFACE_LINK_XML
        )
