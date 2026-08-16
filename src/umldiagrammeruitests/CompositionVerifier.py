
from logging import Logger
from logging import getLogger
from pathlib import Path

from pyautogui import click

from umldiagrammeruitests.BaseVerifier import BaseVerifier
from umldiagrammeruitests.locators.BaseLocator import Location

#
# Removed the IDs;  Also, removed the ModelLink name
#
GOLDEN_COMPOSITION_XML: str = (
    "<?xml version='1.0' encoding='iso-8859-1'?>\n"
    '<UmlProject fileName="/private/tmp/compositiontest.udt" version="14.0" codePath=".">\n'
    '    <UMLDiagram documentType="Class Document" title="Class Diagram" scrollPositionX="0" scrollPositionY="0" pixelsPerUnitX="20" pixelsPerUnitY="20">\n'
    '        <UmlClass id="" width="107" height="90" x="199" y="152">\n'
    '            <ModelClass id="" name="TheComposer" displayMethods="True" displayParameters="Unspecified" displayConstructor="Unspecified" displayDunderMethods="Unspecified" displayFields="True" displayStereotype="True" fileName="" description="" />\n'
    '        </UmlClass>\n'
    '        <UmlClass id="" width="82" height="90" x="549" y="447">\n'
    '            <ModelClass id="" name="Composed" displayMethods="True" displayParameters="Unspecified" displayConstructor="Unspecified" displayDunderMethods="Unspecified" displayFields="True" displayStereotype="True" fileName="" description="" />\n'
    '        </UmlClass>\n'
    '        <UmlLink id="" fromX="304" fromY="242" toX="549" toY="456" spline="False">\n'
    '            <AssociationName deltaX="0" deltaY="0" />\n'
    '            <SourceCardinality deltaX="0" deltaY="0" />\n'
    '            <DestinationCardinality deltaX="0" deltaY="30" />\n'
    '            <ModelLink name="" type="COMPOSITION" sourceId="" destinationId="" bidirectional="False" sourceCardinalityValue="src Card" destinationCardinalityValue="dst Card" />\n'
    '        </UmlLink>\n'
    '    </UMLDiagram>\n'
    '</UmlProject>'
)
BASENAME:                         str  = 'compositiontest'
COMPOSITION_XML_FILENAME:         str = f'{BASENAME}.xml'
COMPOSITION_PROJECT_FILENAME:     Path = Path(f'/tmp/{BASENAME}.udt')
DECOMPRESSED_COMPOSITION_PROJECT: Path = Path(f'/tmp/{COMPOSITION_XML_FILENAME}')

LOC_WHERE_COMPOSER_IS_CREATED: Location = Location(x=475, y=255)
LOC_WHERE_COMPOSED_IS_CREATED: Location = Location(x=825, y=550)

class CompositionVerifier(BaseVerifier):
    def __init__(self):
        
        super().__init__()
        self.logger: Logger = getLogger(__name__)

    def execute(self):

        super().execute()

        COMPOSITION_PROJECT_FILENAME.unlink(missing_ok=True)
        DECOMPRESSED_COMPOSITION_PROJECT.unlink(missing_ok=True)

        self._bringUmlDiagrammerToForeground()

        self._createUmlClassPair(
            class1Location=LOC_WHERE_COMPOSER_IS_CREATED,
            class1Name='TheComposer',
            class2Location=LOC_WHERE_COMPOSED_IS_CREATED,
            class2Name='Composed'
        )

        self._toolBarClicker.clickComposition()

        composerLocation: Location = self._umlClassLocator.composer
        click(x=composerLocation.x, y=composerLocation.y)
        self.logger.info(f'{composerLocation=}')

        composedLocation: Location = self._umlClassLocator.composed
        click(x=composedLocation.x, y=composedLocation.y)
        self.logger.info(f'{composedLocation=}')

        self._saveAsProject.execute(projectFileName=str(COMPOSITION_PROJECT_FILENAME))

        self._verifyTest(
            projectFileName=COMPOSITION_PROJECT_FILENAME,
            decompressedProjectFileName=DECOMPRESSED_COMPOSITION_PROJECT,
            goldenXml=GOLDEN_COMPOSITION_XML
        )
