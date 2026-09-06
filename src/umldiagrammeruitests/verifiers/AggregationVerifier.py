
from logging import Logger
from logging import getLogger
from pathlib import Path

from umldiagrammeruitests.verifiers.AggregationCreator import AggregationCreator

#
# Removed the IDs;  Also, removed the ModelLink name
#
GOLDEN_AGGREGATION_XML: str = (
    "<?xml version='1.0' encoding='iso-8859-1'?>\n"
    '<UmlProject fileName="/private/tmp/AggregationTest.udt" version="14.0" codePath=".">\n'
    '    <UMLDiagram documentType="Class Document" title="Class Diagram" scrollPositionX="0" scrollPositionY="0" pixelsPerUnitX="20" pixelsPerUnitY="20">\n'
    '        <UmlClass id="" width="113" height="90" x="199" y="152">\n'
    '            <ModelClass id="" name="TheAggregator" stereotype="noStereotype" displayMethods="True" displayParameters="Unspecified" displayConstructor="Unspecified" displayDunderMethods="Unspecified" displayFields="True" displayStereotype="True" fileName="" description="" />\n'
    '        </UmlClass>\n'
    '        <UmlClass id="" width="88" height="90" x="549" y="447">\n'
    '            <ModelClass id="" name="Aggregated" stereotype="noStereotype" displayMethods="True" displayParameters="Unspecified" displayConstructor="Unspecified" displayDunderMethods="Unspecified" displayFields="True" displayStereotype="True" fileName="" description="" />\n'
    '        </UmlClass>\n'
    '        <UmlLink id="" fromX="307" fromY="242" toX="549" toY="454" spline="False">\n'
    '            <AssociationName width="75" height="24" deltaX="0" deltaY="0" />\n'
    '            <SourceCardinality width="75" height="24" deltaX="0" deltaY="0" />\n'
    '            <DestinationCardinality width="75" height="24" deltaX="0" deltaY="30" />\n'
    '            <ModelLink name="" type="AGGREGATION" sourceId="" destinationId="" bidirectional="False" sourceCardinalityValue="src Card" destinationCardinalityValue="dst Card" />\n'
    '        </UmlLink>\n'
    '    </UMLDiagram>\n'
    '</UmlProject>'
)

BASENAME:                         str  = 'AggregationTest'
AGGREGATION_XML_FILENAME:         str = f'{BASENAME}.xml'
AGGREGATION_PROJECT_FILENAME:     Path = Path(f'/tmp/{BASENAME}.udt')
DECOMPRESSED_AGGREGATION_PROJECT: Path = Path(f'/tmp/{AGGREGATION_XML_FILENAME}')


class AggregationVerifier(AggregationCreator):
    
    def __init__(self):
        super().__init__(aggregationProjectFileName=AGGREGATION_PROJECT_FILENAME, decompressedAggregationFileName=DECOMPRESSED_AGGREGATION_PROJECT)
        self.logger: Logger = getLogger(__name__)

    def execute(self):

        super().execute()

        self._bringUmlDiagrammerToForeground()

        self._createAggregationDiagram()

        self._verifyTest(
            projectFileName=AGGREGATION_PROJECT_FILENAME,
            decompressedProjectFileName=DECOMPRESSED_AGGREGATION_PROJECT,
            goldenXml=GOLDEN_AGGREGATION_XML
        )
