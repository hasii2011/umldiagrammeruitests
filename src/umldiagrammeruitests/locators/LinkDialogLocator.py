
from logging import Logger
from logging import getLogger

from pathlib import Path

from codeallybasic.ResourceManager import ResourceManager

from umldiagrammeruitests.locators.BaseLocator import BaseLocator
from umldiagrammeruitests.locators.BaseLocator import BoundingBox
from umldiagrammeruitests.locators.BaseLocator import Location

# noinspection SpellCheckingInspection
PACKAGE_NAME:  str = 'umldiagrammeruitests.resources.linkdialog'
# noinspection SpellCheckingInspection
RESOURCE_PATH: str = 'umldiagrammeruitests/resources/linkdialog'

LINK_DIALOG_CONFIDENCE: float = 0.90


class LinkDialogLocator(BaseLocator):

    def __init__(self, confidence: float = LINK_DIALOG_CONFIDENCE, grayScale: bool = True):

        resourcePath: Path = ResourceManager.computeResourcePath(resourcePath=RESOURCE_PATH, packageName=PACKAGE_NAME)

        super().__init__(confidence=confidence, grayScale=grayScale, resourcePath=resourcePath)
        self.logger: Logger = getLogger(__name__)

        self.logger.info(f'Location Confidence: {self._confidence:.2f}')

    @property
    def okButton(self) -> Location:
        return self._locate('OkButton.png')

    @property
    def sourceCardinalityTextInput(self) -> Location:
        return self._locate('SourceCardinalityTextInput.png')

    @property
    def destinationCardinalityTextInput(self) -> Location:
        return self._locate('DestinationCardinalityTextInput.png')

    @property
    def associationNameTextInput(self) -> Location:
        return self._locate('AssociationNameTextInput.png')

    @property
    def associationNameLabel(self) -> Location:
        return self._locate('AssociationNameLabel.png')

    @property
    def associationNameLabelSelected(self) -> BoundingBox:
        """
        We are returning the bounding box of the image !!

        Returns:  A Bounding box

        """
        return self._locateBoundingBox('AssociationNameLabelSelected.png')

    @property
    def sourceCardinalityLabel(self) -> Location:
        return self._locate('SourceCardinalityLabel.png')

    @property
    def sourceCardinalityLabelSelected(self) -> BoundingBox:
        """
        We are returning the bounding box of the image !!

        Returns:  A Bounding box
        """
        return self._locateBoundingBox('SourceCardinalityLabelSelected.png')

    @property
    def destinationCardinalityLabel(self) -> Location:
        return self._locate('DestinationCardinalityLabel.png')

    @property
    def destinationCardinalityLabelSelected(self) -> BoundingBox:
        """
        We are returning the bounding box of the image !!

        Returns:  A Bounding box

        """
        return self._locateBoundingBox('DestinationCardinalityLabelSelected.png')

