
from logging import Logger
from logging import getLogger

from codeallybasic.ResourceManager import ResourceManager

from umldiagrammeruitests.locators.BaseLocator import BaseLocator
from umldiagrammeruitests.locators.BaseLocator import Location

CLASS_LOCATOR_CONFIDENCE: float = 0.90


PACKAGE_NAME:  str = 'umldiagrammeruitests.resources.umlclasslocator'
RESOURCE_PATH: str = 'umldiagrammeruitests/resources/umlclasslocator'


class UmlClassLocator(BaseLocator):

    def __init__(self, confidence: float = CLASS_LOCATOR_CONFIDENCE, grayScale: bool = True):
        """

        Args:
            confidence:  The confidence level for the look ups
        """
        resourcePath = ResourceManager.computeResourcePath(resourcePath=RESOURCE_PATH, packageName=PACKAGE_NAME)

        super().__init__(confidence=confidence, grayScale=grayScale, resourcePath=resourcePath)
        self.logger: Logger = getLogger(__name__)

        self.logger.info(f'Location Confidence: {self._confidence:.2f}')

    @property
    def aggregator(self) -> Location:
        return self._locate('Aggregator.png')

    @property
    def aggregated(self) -> Location:
        return self._locate('Aggregated.png')

    @property
    def composer(self) -> Location:
        return self._locate('Composer.png')

    @property
    def composed(self) -> Location:
        return self._locate('Composed.png')

    @property
    def baseClass(self) -> Location:
        return self._locate('BaseClass.png')

    @property
    def subClass(self) -> Location:
        return self._locate('SubClass.png')
