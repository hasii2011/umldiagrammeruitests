
from logging import Logger
from logging import getLogger
from pathlib import Path

from pyautogui import click

from umldiagrammeruitests.BaseVerifier import BaseVerifier
from umldiagrammeruitests.locators.BaseLocator import Location

#
# Removed the IDs
#
GOLDEN_INHERITANCE_XML: str = (
    "<?xml version='1.0' encoding='iso-8859-1'?>\n"
    '<UmlProject fileName="/private/tmp/inheritancetest.udt" version="14.0" codePath=".">\n'
    '    <UMLDiagram documentType="Class Document" title="Class Diagram" scrollPositionX="0" scrollPositionY="0" pixelsPerUnitX="20" pixelsPerUnitY="20">\n'
    '        <UmlClass id="" width="110" height="90" x="124" y="97">\n'
    '            <ModelClass id="" name="TheBaseClass" displayMethods="True" displayParameters="Unspecified" displayConstructor="Unspecified" displayDunderMethods="Unspecified" displayFields="True" displayStereotype="True" fileName="" description="" />\n'
    '        </UmlClass>\n'
    '        <UmlClass id="" width="72" height="90" x="624" y="397">\n'
    '            <ModelClass id="" name="SubClass" displayMethods="True" displayParameters="Unspecified" displayConstructor="Unspecified" displayDunderMethods="Unspecified" displayFields="True" displayStereotype="True" fileName="" description="" />\n'
    '        </UmlClass>\n'
    '        <UmlLink id="" fromX="624" fromY="420" toX="234" toY="176" spline="False">\n'
    '            <ModelLink name="" type="INHERITANCE" sourceId="" destinationId="" bidirectional="False" sourceCardinalityValue="" destinationCardinalityValue="" />\n'
    '        </UmlLink>\n'
    '    </UMLDiagram>\n'
    '</UmlProject>'
)

BASENAME:                 str  = 'inheritancetest'
INHERITANCE_XML_FILENAME: str = f'{BASENAME}.xml'

INHERITANCE_PROJECT_FILENAME:     Path = Path(f'/tmp/{BASENAME}.udt')
DECOMPRESSED_INHERITANCE_PROJECT: Path = Path(f'/tmp/{INHERITANCE_XML_FILENAME}')

LOC_CREATE_BASE_CLASS: Location = Location(x=400, y=200)
LOC_CREATE_SUB_CLASS:  Location = Location(x=900, y=500)


SUBCLASS_NAME:    str = 'SubClass'
BASECLASS_NAME:   str = 'TheBaseClass'

class InheritanceVerifier(BaseVerifier):
    
    def __init__(self):
        
        super().__init__()
        self.logger: Logger = getLogger(__name__)

    def execute(self):

        super().execute()

        INHERITANCE_PROJECT_FILENAME.unlink(missing_ok=True)
        DECOMPRESSED_INHERITANCE_PROJECT.unlink(missing_ok=True)

        self._bringUmlDiagrammerToForeground()

        self._createUmlClassPair(
            class1Location=LOC_CREATE_BASE_CLASS,
            class1Name=BASECLASS_NAME,
            class2Location=LOC_CREATE_SUB_CLASS,
            class2Name=SUBCLASS_NAME
        )

        self._toolBarClicker.clickInheritance()

        subClassLocation: Location = self._umlClassLocator.subClass
        click(x=subClassLocation.x, y=subClassLocation.y)
        self.logger.info(f'{subClassLocation=}')

        baseClassLocation: Location = self._umlClassLocator.baseClass
        click(x=baseClassLocation.x, y=baseClassLocation.y)
        self.logger.info(f'{baseClassLocation=}')

        self._saveAsProject.execute(projectFileName=str(INHERITANCE_PROJECT_FILENAME))

        self._verifyTest(
            projectFileName=INHERITANCE_PROJECT_FILENAME,
            decompressedProjectFileName=DECOMPRESSED_INHERITANCE_PROJECT,
            goldenXml=GOLDEN_INHERITANCE_XML
        )
