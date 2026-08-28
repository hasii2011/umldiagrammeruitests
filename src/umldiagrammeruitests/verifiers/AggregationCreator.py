

from logging import Logger
from logging import getLogger

from pathlib import Path

from pyautogui import click

from umldiagrammeruitests.locators.BaseLocator import Location
from umldiagrammeruitests.verifiers.BaseVerifier import BaseVerifier


AGGREGATOR_LOCATION: Location = Location(x=475, y=255)
AGGREGATED_LOCATION: Location = Location(x=825, y=550)

class AggregationCreator(BaseVerifier):

    def __init__(self, aggregationProjectFileName: Path, decompressedAggregationFileName: Path):
        
        super().__init__()
        self.logger: Logger = getLogger(__name__)

        self._aggregationProjectFileName:      Path = aggregationProjectFileName
        self._decompressedAggregationFileName: Path = decompressedAggregationFileName

    def execute(self):

        super().execute()

        self._aggregationProjectFileName.unlink(missing_ok=True)
        self._decompressedAggregationFileName.unlink(missing_ok=True)

    def _createAggregationDiagram(self):
        """
        To reuse for other tests

        """
        self._createUmlClassPair(
            class1Location=AGGREGATOR_LOCATION,
            class1Name='TheAggregator',
            class2Location=AGGREGATED_LOCATION,
            class2Name='Aggregated'
        )

        self._toolBarClicker.clickAggregation()

        aggregatorLocation: Location = self._umlClassLocator.aggregator
        click(x=aggregatorLocation.x, y=aggregatorLocation.y)
        self.bLogger.info(f'{aggregatorLocation=}')

        aggregatedLocation: Location = self._umlClassLocator.aggregated
        click(x=aggregatedLocation.x, y=aggregatedLocation.y)
        self.bLogger.info(f'{aggregatedLocation=}')

        self._saveAsProject.execute(projectFileName=str(self._aggregationProjectFileName))
