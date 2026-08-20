
from logging import Logger
from logging import getLogger

from codeallybasic.ResourceManager import ResourceManager

from umldiagrammeruitests.locators.BaseLocator import BaseLocator
from umldiagrammeruitests.locators.BaseLocator import Location

# noinspection SpellCheckingInspection
PACKAGE_NAME:  str = 'umldiagrammeruitests.resources.common'
# noinspection SpellCheckingInspection
RESOURCE_PATH: str = 'umldiagrammeruitests/resources/common'

COMMON_CONFIDENCE: float = 0.90


class CommonImageLocator(BaseLocator):
    """
    Locates common images on screen.
    """
    def __init__(self, confidence: float = COMMON_CONFIDENCE, grayScale: bool = True):
        """

        Args:
            confidence:  The confidence level for the look ups
        """
        resourcePath = ResourceManager.computeResourcePath(resourcePath=RESOURCE_PATH, packageName=PACKAGE_NAME)

        super().__init__(confidence=confidence, grayScale=grayScale, resourcePath=resourcePath)
        self.logger: Logger = getLogger(__name__)

        self.logger.info(f'Location Confidence: {self._confidence:.2f}')

    @property
    def saveAsProjectNameTextInput(self) -> Location:
        return self._locate('SaveAsProjectNameTextInput.png')

    @property
    def saveProjectAsButton(self) -> Location:
        return self._locate('SaveProjectAsButton.png')

    @property
    def defaultNoteText(self) -> Location:
        return self._locate('DefaultNoteText.png')

    @property
    def okButton(self) -> Location:
        return self._locate('OkButton.png')

    @property
    def classWithNote(self) -> Location:
        return self._locate('ClassWithNote.png')

    @property
    def uiTestNote(self) -> Location:
        return self._locate('UITestNote.png')
