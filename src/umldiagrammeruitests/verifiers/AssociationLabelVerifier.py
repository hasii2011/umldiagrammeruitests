
from logging import Logger
from logging import getLogger
from pathlib import Path

from click import secho

from umldiagrammeruitests.MacOsDoubleClickHandler import MacOsDoubleClickHandler
from umldiagrammeruitests.locators.BaseLocator import Location
from umldiagrammeruitests.verifiers.AggregationCreator import AggregationCreator

BASENAME:                         str  = 'AssociationLabelTest'
AGGREGATION_XML_FILENAME:         str = f'{BASENAME}.xml'
AGGREGATION_PROJECT_FILENAME:     Path = Path(f'/tmp/{BASENAME}.udt')
DECOMPRESSED_AGGREGATION_PROJECT: Path = Path(f'/tmp/{AGGREGATION_XML_FILENAME}')


class AssociationLabelVerifier(AggregationCreator):

    def __init__(self):
        super().__init__(aggregationProjectFileName=AGGREGATION_PROJECT_FILENAME, decompressedAggregationFileName=DECOMPRESSED_AGGREGATION_PROJECT)
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
