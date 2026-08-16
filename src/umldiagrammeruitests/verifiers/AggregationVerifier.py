
from logging import Logger
from logging import getLogger

from pathlib import Path

from pyautogui import click

from umldiagrammeruitests.verifiers.BaseVerifier import BaseVerifier
from umldiagrammeruitests.locators.BaseLocator import Location

#
# Removed the IDs;  Also, removed the ModelLink name
#
GOLDEN_AGGREGATION_XML: str = (
    "<?xml version='1.0' encoding='iso-8859-1'?>\n"
    '<UmlProject fileName="/private/tmp/aggregationtest.udt" version="14.0" codePath=".">\n'
    '    <UMLDiagram documentType="Class Document" title="Class Diagram" scrollPositionX="0" scrollPositionY="0" pixelsPerUnitX="20" pixelsPerUnitY="20">\n'
    '        <UmlClass id="" width="113" height="90" x="199" y="152">\n'
    '            <ModelClass id="" name="TheAggregator" displayMethods="True" displayParameters="Unspecified" displayConstructor="Unspecified" displayDunderMethods="Unspecified" displayFields="True" displayStereotype="True" fileName="" description="" />\n'
    '        </UmlClass>\n'
    '        <UmlClass id="" width="88" height="90" x="549" y="447">\n'
    '            <ModelClass id="" name="Aggregated" displayMethods="True" displayParameters="Unspecified" displayConstructor="Unspecified" displayDunderMethods="Unspecified" displayFields="True" displayStereotype="True" fileName="" description="" />\n'
    '        </UmlClass>\n'
    '        <UmlLink id="" fromX="307" fromY="242" toX="549" toY="454" spline="False">\n'
    '            <AssociationName deltaX="0" deltaY="0" />\n'
    '            <SourceCardinality deltaX="0" deltaY="0" />\n'
    '            <DestinationCardinality deltaX="0" deltaY="30" />\n'
    '            <ModelLink name="" type="AGGREGATION" sourceId="" destinationId="" bidirectional="False" sourceCardinalityValue="src Card" destinationCardinalityValue="dst Card" />\n'
    '        </UmlLink>\n'
    '    </UMLDiagram>\n'
    '</UmlProject>'
)
BASENAME:                         str  = 'aggregationtest'
AGGREGATION_XML_FILENAME:         str = f'{BASENAME}.xml'
AGGREGATION_PROJECT_FILENAME:     Path = Path(f'/tmp/{BASENAME}.udt')
DECOMPRESSED_AGGREGATION_PROJECT: Path = Path(f'/tmp/{AGGREGATION_XML_FILENAME}')

LOC_WHERE_AGGREGATOR_IS_CREATED: Location = Location(x=475, y=255)
LOC_WHERE_AGGREGATED_IS_CREATED: Location = Location(x=825, y=550)


class AggregationVerifier(BaseVerifier):
    
    def __init__(self):
        super().__init__()
        self.logger: Logger = getLogger(__name__)

    def execute(self):

        super().execute()

        AGGREGATION_PROJECT_FILENAME.unlink(missing_ok=True)
        DECOMPRESSED_AGGREGATION_PROJECT.unlink(missing_ok=True)

        self._bringUmlDiagrammerToForeground()

        self._createUmlClassPair(
            class1Location=LOC_WHERE_AGGREGATOR_IS_CREATED,
            class1Name='TheAggregator',
            class2Location=LOC_WHERE_AGGREGATED_IS_CREATED,
            class2Name='Aggregated'
        )

        self._toolBarClicker.clickAggregation()

        aggregatorLocation: Location = self._umlClassLocator.aggregator
        click(x=aggregatorLocation.x, y=aggregatorLocation.y)
        self.logger.info(f'{aggregatorLocation=}')

        aggregatedLocation: Location = self._umlClassLocator.aggregated
        click(x=aggregatedLocation.x, y=aggregatedLocation.y)
        self.logger.info(f'{aggregatedLocation=}')

        self._saveAsProject.execute(projectFileName=str(AGGREGATION_PROJECT_FILENAME))

        self._verifyTest(
            projectFileName=AGGREGATION_PROJECT_FILENAME,
            decompressedProjectFileName=DECOMPRESSED_AGGREGATION_PROJECT,
            goldenXml=GOLDEN_AGGREGATION_XML
        )
