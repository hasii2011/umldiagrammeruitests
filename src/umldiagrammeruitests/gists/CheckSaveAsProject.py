#!/usr/bin/env python
# /// script
# dependencies = ['pyautogui', 'pillow', 'umlshapes', 'opencv-python', 'pyperclip']
# ///
from os import sep as osSep

from pathlib import Path

from umldiagrammeruitests.Common import setupLogging
from umldiagrammeruitests.SaveAsProject import SaveAsProject
from umldiagrammeruitests.ToolBarClicker import ToolBarClicker
from umldiagrammeruitests.locators.CommonImageLocator import CommonImageLocator

BASENAME:                   str = 'uiclasstest'
CLASS_PROJECT_FILENAME:     Path = Path(f'{osSep}tmp{osSep}{BASENAME}.udt')

if __name__ == '__main__':

    import pyautogui

    pyautogui.PAUSE = 0.5
    pyautogui.FAILSAFE = True

    setupLogging()

    invokeSaveAsProject: SaveAsProject = SaveAsProject(
        commonImageLocator=CommonImageLocator(),
        toolBarClicker=ToolBarClicker(),
    )

    invokeSaveAsProject.execute(projectFileName=str(CLASS_PROJECT_FILENAME))
