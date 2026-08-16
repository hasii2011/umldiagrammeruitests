
from logging import Logger
from logging import getLogger

from pathlib import Path

from codeallybasic.ResourceManager import ResourceManager

from umldiagrammeruitests.locators.BaseLocator import BaseLocator

from umldiagrammeruitests.locators.BaseLocator import Location

# noinspection SpellCheckingInspection
PACKAGE_NAME:  str = 'umldiagrammeruitests.resources.checkclassimages'
# noinspection SpellCheckingInspection
RESOURCE_PATH: str = 'umldiagrammeruitests/resources/checkclassimages'

LOCATE_CONFIDENCE: float = 0.90

class ClassDialogLocator(BaseLocator):
    def __init__(self, confidence: float = LOCATE_CONFIDENCE, grayScale: bool = False):
        """

        Args:
            confidence:  The confidence level for the look ups
        """
        self.logger: Logger = getLogger(__name__)

        resourcePath: Path = ResourceManager.computeResourcePath(
            resourcePath=RESOURCE_PATH,
            packageName=PACKAGE_NAME
        )

        super().__init__(confidence=confidence, grayScale=grayScale, resourcePath=resourcePath)

        self.logger.info(f'Location Confidence: {self._confidence:.2f}')

    @property
    def classNameTextInput(self) -> Location:
        return self._locate(bareFileName='ClassNameTextInput.png')

    @property
    def addMethodButton(self) -> Location:
        return self._locate(bareFileName='ClickAddMethod.png')

    @property
    def addParameterButton(self) -> Location:
        return self._locate(bareFileName='ClickAddParameter.png')

    @property
    def parameterNameTextInput(self) -> Location:
        return self._locate('ParameterNameTextInput.png')

    @property
    def clickParameterOkButton(self) -> Location:
        return self._locate('ClickParameterOkButton.png')

    @property
    def clickMethodOkButton(self) -> Location:
        return self._locate('ClickMethodOkButton.png')

    @property
    def clickClassOkButton(self) -> Location:
        return self._locate('ClickClassOkButton.png')

    @property
    def clickAddFieldButton(self) -> Location:
        return self._locate('ClickAddFieldButton.png')

    @property
    def publicFieldRadioButton(self) -> Location:
        return self._locate('PublicFieldRadioButton.png')

    @property
    def fieldNameTextInput(self) -> Location:
        return self._locate('FieldNameTextInput.png')

    @property
    def clickFieldOkButton(self) -> Location:
        return self._locate('ClickFieldOkButton.png')

    @property
    def classShape(self) -> Location:
        return self._locate('ClassShape.png')

    @property
    def classShapeContextMenu(self) -> Location:
        return self._locate('ClassShapeContextMenu.png')
