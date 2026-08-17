
from logging import Logger
from logging import getLogger

from os import sep as osSep

from pathlib import Path

from pyautogui import click
from pyautogui import press
from pyautogui import typewrite

from umldiagrammeruitests.Common import DEFAULT_METHOD_NAME
from umldiagrammeruitests.Common import DOUBLE_CLICK_INTERVAL
from umldiagrammeruitests.Common import TYPE_WRITE_INTERVAL
from umldiagrammeruitests.locators.BaseLocator import Location
from umldiagrammeruitests.verifiers.BaseVerifier import BaseVerifier

WELL_KNOWN_CLASS_NAME: str = 'ClassName1'

#
# Removed the IDs
#
GOLDEN_CLASS_XML: str = (
    "<?xml version='1.0' encoding='iso-8859-1'?>\n"
    '<UmlProject fileName="/private/tmp/uiclasstest.udt" version="14.0" codePath=".">\n'
    '    <UMLDiagram documentType="Class Document" title="Class Diagram" scrollPositionX="0" scrollPositionY="0" pixelsPerUnitX="20" pixelsPerUnitY="20">\n'
    '        <UmlClass id="" width="325" height="150" x="404" y="267">\n'
    '            <ModelClass id="" name="ClassName1" displayMethods="True" displayParameters="Display Parameters" displayConstructor="Unspecified" displayDunderMethods="Unspecified" displayFields="True" displayStereotype="True" fileName="" description="">\n'
    '                <ModelMethod name="MethodName" visibility="PUBLIC" returnType="">\n'
    '                    <SourceCode />\n'
    '                    <ModelParameter name="floatParameter" parameterType="float" defaultValue="42.0" />\n'
    '                </ModelMethod>\n'
    '                <ModelField name="publicField" visibility="PUBLIC" fieldType="int" defaultValue="42" />\n'
    '            </ModelClass>\n'
    '        </UmlClass>\n'
    '    </UMLDiagram>\n'
    '</UmlProject>'
)

BASENAME:                   str = 'uiclasstest'
CLASS_XML_FILENAME:         str = f'{BASENAME}.xml'

CLASS_PROJECT_FILENAME:     Path = Path(f'{osSep}tmp{osSep}{BASENAME}.udt')
DECOMPRESSED_CLASS_PROJECT: Path = Path(f'{osSep}tmp{osSep}{CLASS_XML_FILENAME}')

LOC_WHERE_CLASS_IS_CREATED: Location = Location(x=680, y=370)

HACK_ADJUST_ADD_METHOD_BUTTON_Y: int = 40
HACK_ADJUST_ADD_FIELD_BUTTON_Y:  int = 40

HACK_ADJUST_PARAMETER_TEXT_INPUT_X:  int = 5
HACK_ADJUST_PARAMETER_TEXT_INPUT_Y:  int = 5


class BasicClassVerifier(BaseVerifier):
    def __init__(self):
        super().__init__()
        self.logger: Logger = getLogger(__name__)

    def execute(self):

        super().execute()

        CLASS_PROJECT_FILENAME.unlink(missing_ok=True)
        DECOMPRESSED_CLASS_PROJECT.unlink(missing_ok=True)

        self._bringUmlDiagrammerToForeground()

        self._toolBarClicker.clickNewClass()

        click(x=LOC_WHERE_CLASS_IS_CREATED.x, y=LOC_WHERE_CLASS_IS_CREATED.y)

        self._renameUmlClass(newClassName=WELL_KNOWN_CLASS_NAME)

        addMethodButtonLocation: Location = self._classDialogLocator.addMethodButton
        click(x=addMethodButtonLocation.x, y=addMethodButtonLocation.y + HACK_ADJUST_ADD_METHOD_BUTTON_Y)  # Cheat from center

        self._addParameterMethod()
        methodOkButtonLocation: Location = self._classDialogLocator.clickMethodOkButton
        click(x=methodOkButtonLocation.x,    y=methodOkButtonLocation.y)

        self._addPublicField()

        clickClassOkButton: Location = self._classDialogLocator.clickClassOkButton
        click(x=clickClassOkButton.x, y=clickClassOkButton.y)

        classShapeLocation: Location = self._classDialogLocator.classShape
        click(x=classShapeLocation.x,  y=classShapeLocation.y, button='right')

        classContextMenuLocation: Location = self._classDialogLocator.classShapeContextMenu
        click(x=classContextMenuLocation.x, y=classContextMenuLocation.y)

        self._saveAsProject.execute(projectFileName=str(CLASS_PROJECT_FILENAME))

        self._verifyTest(
            projectFileName=CLASS_PROJECT_FILENAME,
            decompressedProjectFileName=DECOMPRESSED_CLASS_PROJECT,
            goldenXml=GOLDEN_CLASS_XML
        )

    def _addParameterMethod(self):

        addParameterButtonLocation: Location = self._classDialogLocator.addParameterButton
        click(x=addParameterButtonLocation.x, y=addParameterButtonLocation.y)

        parameterNameLocation: Location = self._classDialogLocator.parameterNameTextInput
        click(
            x=parameterNameLocation.x + HACK_ADJUST_PARAMETER_TEXT_INPUT_X,
            y=parameterNameLocation.y + HACK_ADJUST_PARAMETER_TEXT_INPUT_Y,
            clicks=2,
            interval=DOUBLE_CLICK_INTERVAL
        )
        press('backspace', presses=len(DEFAULT_METHOD_NAME))
        typewrite('floatParameter', interval=TYPE_WRITE_INTERVAL)

        press('tab')
        typewrite('float', interval=TYPE_WRITE_INTERVAL)

        press('tab')
        typewrite('42.0', interval=TYPE_WRITE_INTERVAL)

        parameterOkButtonLocation: Location = self._classDialogLocator.clickParameterOkButton
        click(x=parameterOkButtonLocation.x, y=parameterOkButtonLocation.y + 10)

    def _addPublicField(self):

        addFieldButtonLocation: Location = self._classDialogLocator.clickAddFieldButton
        click(x=addFieldButtonLocation.x, y=addFieldButtonLocation.y + HACK_ADJUST_ADD_FIELD_BUTTON_Y)

        publicFieldRBLocation: Location = self._classDialogLocator.publicFieldRadioButton
        click(x=publicFieldRBLocation.x, y=publicFieldRBLocation.y)

        press('backspace')      # text input still has focus

        typewrite('publicField', interval=TYPE_WRITE_INTERVAL)
        press('right', presses=3)

        press('tab')
        typewrite('int', interval=TYPE_WRITE_INTERVAL)

        press('tab')
        typewrite('42', interval=TYPE_WRITE_INTERVAL)

        fieldOkButtonLocation: Location = self._classDialogLocator.clickFieldOkButton
        click(x=fieldOkButtonLocation.x, y=fieldOkButtonLocation.y)
