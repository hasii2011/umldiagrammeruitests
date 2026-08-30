
from logging import Logger
from logging import getLogger

from pathlib import Path

from codeallybasic.ResourceManager import ResourceManager

from umldiagrammeruitests.locators.BaseLocator import BaseLocator
from umldiagrammeruitests.locators.BaseLocator import Location

# noinspection SpellCheckingInspection
PACKAGE_NAME:  str = 'umldiagrammeruitests.resources.toolbaricons'
# noinspection SpellCheckingInspection
RESOURCE_PATH: str = 'umldiagrammeruitests/resources/toolbaricons'

LOCATE_CONFIDENCE: float = 0.90


class ToolBarIconLocator(BaseLocator):
    """
    Locates toolbar icon images on screen.
    """
    def __init__(self, confidence: float = LOCATE_CONFIDENCE, grayScale: bool = True):
        """

        Args:
            confidence:  The confidence level for the look ups
        """
        resourcePath: Path = ResourceManager.computeResourcePath(resourcePath=RESOURCE_PATH, packageName=PACKAGE_NAME)

        super().__init__(confidence=confidence, grayScale=grayScale, resourcePath=resourcePath)
        self.logger: Logger = getLogger(__name__)

        self.logger.info(f'Location Confidence: {self._confidence:.2f}')

    @property
    def aggregationLink(self) -> Location:
        return self._locate(baseFileName='AggregationLink.png')

    @property
    def associationLink(self) -> Location:
        return self._locate(baseFileName='AssociationLink.png')

    @property
    def compositionLink(self) -> Location:
        return self._locate(baseFileName='CompositionLink.png')

    @property
    def inheritanceLink(self) -> Location:
        return self._locate(baseFileName='InheritanceLink.png')

    @property
    def interfaceLink(self) -> Location:
        return self._locate(baseFileName='InterfaceLink.png')

    @property
    def newActor(self) -> Location:
        return self._locate(baseFileName='NewActor.png')

    @property
    def newClass(self) -> Location:
        return self._locate(baseFileName='NewClass.png')

    @property
    def newClassDiagram(self) -> Location:
        return self._locate(baseFileName='NewClassDiagram.png')

    @property
    def newNote(self) -> Location:
        return self._locate(baseFileName='NewNote.png')

    @property
    def newText(self) -> Location:
        return self._locate(baseFileName='NewText.png')

    @property
    def newUseCase(self) -> Location:
        return self._locate(baseFileName='NewUseCase.png')

    @property
    def newUseCaseDiagram(self) -> Location:
        return self._locate(baseFileName='NewUseCaseDiagram.png')

    @property
    def noteLink(self) -> Location:
        return self._locate(baseFileName='NoteLink.png')

    @property
    def saveProject(self) -> Location:
        return self._locate(baseFileName='SaveProject.png')
