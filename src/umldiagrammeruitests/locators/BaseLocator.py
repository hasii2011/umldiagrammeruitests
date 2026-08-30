
from typing import cast

from logging import Logger
from logging import getLogger

from dataclasses import dataclass

from pathlib import Path

# noinspection PyPackageRequirements
from pyscreeze import Box
from pyscreeze import Point

from pyautogui import locateOnScreen
from pyautogui import locateCenterOnScreen
from pyautogui import ImageNotFoundException

@dataclass
class Location:
    x: int = 0
    y: int = 0

@dataclass
class BoundingBox:
    left:   int = 0
    top:    int = 0
    width:  int = 0
    height: int = 0


LOCATION_NOT_SET:      Location    = cast(Location, None)
BOUNDING_BOX_NOT_SET:  BoundingBox = cast(BoundingBox, None)


LOCATE_CONFIDENCE: float    = 0.95

class BaseLocator:
    def __init__(self, confidence: float, grayScale: bool, resourcePath: Path):

        self.baseLogger: Logger = getLogger(__name__)

        self._confidence:   float = confidence
        self._grayScale:    bool  = grayScale
        self._resourcePath: Path  = resourcePath

    def _locate(self, baseFileName: str) -> Location:
        """
        Finds the center of image location on the screen

        On modern Apple Silicon and Retina Macs, the display uses 2 physical pixels for every 1
        logical point (a scale factor of 2):

        Args:
            baseFileName:   The file name of the image

        Returns:  The location on the screen where that image is
        """

        try:
            path:        Path         = self._resourcePath / baseFileName
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
            self.baseLogger.error(f'Cannot find: {baseFileName} on screen.')
            raise e

        return LOCATION_NOT_SET

    def _locateBoundingBox(self, baseFileName: str) -> BoundingBox:
        """
        On modern Apple Silicon and Retina Macs, the display uses 2 physical pixels for every 1
        logical point (a scale factor of 2):

        Args:
            baseFileName:  The file name of the image

        Returns: The bounding box for the image

        """

        try:
            path:      Path       = self._resourcePath / baseFileName
            targetBox: Box | None = locateOnScreen(
                str(path),
                confidence=self._confidence,
                grayscale=self._grayScale
            )
            if targetBox is not None:
                logicalLeft:   int = int(targetBox.left / 2)
                logicalTop:    int = int(targetBox.top / 2)
                logicalWidth:  int = int(targetBox.width / 2)
                logicalHeight: int = int(targetBox.height / 2)

                return BoundingBox(
                    left=logicalLeft,
                    top=logicalTop,
                    width=logicalWidth,
                    height=logicalHeight
                )
        except ImageNotFoundException as e:
            self.baseLogger.error(f'Cannot find: {baseFileName} on screen.')
            raise e

        return BOUNDING_BOX_NOT_SET
