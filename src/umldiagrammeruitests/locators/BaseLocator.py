
from typing import cast

from logging import Logger
from logging import getLogger

from dataclasses import dataclass

from pathlib import Path

# noinspection PyPackageRequirements
from pyscreeze import Point
from pyautogui import locateCenterOnScreen
from pyautogui import ImageNotFoundException

@dataclass
class Location:
    x: int = 0
    y: int = 0


LOCATION_NOT_SET:  Location = cast(Location, None)

LOCATE_CONFIDENCE: float    = 0.95

class BaseLocator:
    def __init__(self, confidence: float, grayScale: bool, resourcePath: Path):

        self.baseLogger: Logger = getLogger(__name__)

        self._confidence:   float = confidence
        self._grayScale:    bool  = grayScale
        self._resourcePath: Path  = resourcePath

    def _locate(self, bareFileName: str) -> Location:
        """
        Finds the image location on the screen
        Args:
            bareFileName:   The file name of the image

        Returns:  The location on the screen where that image is
        """

        try:
            path:        Path         = self._resourcePath / bareFileName
            targetPoint: Point | None = locateCenterOnScreen(
                str(path),
                confidence=self._confidence,
                grayscale=self._grayScale
            )

            if targetPoint is not None:
                # Divide by 2 on macOS Retina displays to convert physical pixels to logical points
                logicalX: int = int(targetPoint.x / 2)
                logicalY: int = int(targetPoint.y / 2)
                return Location(x=logicalX, y=logicalY)
        except ImageNotFoundException as e:
            self.baseLogger.error(f'Cannot find: {bareFileName} on screen.')
            raise e

        return LOCATION_NOT_SET
