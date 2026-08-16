
from typing import Any
from typing import Callable

import logging
import logging.config

from functools import wraps

from json import loads as jsonLoads

from importlib.resources import files
from importlib.resources.abc import Traversable

from click import group
from click import pass_context
from click import pass_obj
from click import secho
from click import version_option
from click import ClickException

from pyautogui import ImageNotFoundException

from umldiagrammeruitests.AggregationTest import AggregationTest
from umldiagrammeruitests.Common import PAUSE_AFTER_EACH_CALL
from umldiagrammeruitests.commands.Environment import Environment

RESOURCES_PACKAGE_NAME:       str = 'umldiagrammeruitests.resources'
JSON_LOGGING_CONFIG_FILENAME: str = 'loggingConfiguration.json'

__version__: str = '0.5'

def setUpLogging():
    """
    """
    traversable: Traversable = files(RESOURCES_PACKAGE_NAME) / JSON_LOGGING_CONFIG_FILENAME

    loggingConfigContent:    str  = traversable.read_text(encoding='utf-8')
    configurationDictionary: dict = jsonLoads(loggingConfigContent)

    logging.config.dictConfig(configurationDictionary)
    logging.logProcesses = False
    logging.logThreads = False

def handleUiTestErrors(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that catches ImageNotFoundException and formats Click output.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except ImageNotFoundException as err:
            secho(f'Image Lookup Failure: {err}', fg='red', bold=True)
            raise ClickException(f'Missing image on screen: {err}')
    return wrapper

@group(name='uitest')
@version_option(version=f'{__version__}', message='%(prog)s version %(version)s')
@pass_context
def uitest(ctx, verbose: bool = False):
    """
    \b

    \b

    \b

    \b
    """
    setUpLogging()

    environment: Environment = Environment(verbose=verbose)

    ctx.obj = environment

    # I do not follow my global import convention
    import pyautogui
    pyautogui.PAUSE    = PAUSE_AFTER_EACH_CALL
    pyautogui.FAILSAFE = True


@uitest.command(name='inheritance')
@pass_obj
@handleUiTestErrors
def inheritance(environment: Environment):
    """
    Signs the internal python zipfile;  May optionally remove some bad files in test/zipimport_data
    """
    secho(f'I am here -- {environment=}')


@uitest.command(name='composition')
@pass_obj
@handleUiTestErrors
def composition(environment: Environment):
    """
    Signs the internal python zipfile;  May optionally remove some bad files in test/zipimport_data
    """
    secho(f'I am here -- {environment=}')


@uitest.command(name='aggregation')
@pass_obj
@handleUiTestErrors
def aggregation(environment: Environment):
    """
    Execute the create an aggregation test
    """
    aggregationTest: AggregationTest = AggregationTest()
    aggregationTest.execute()


@uitest.command(name='checkClass')
@pass_obj
@handleUiTestErrors
def checkClass(environment: Environment):
    """
    Signs the internal python zipfile;  May optionally remove some bad files in test/zipimport_data
    """
    secho(f'I am here -- {environment=}')


if __name__ == '__main__':
    # noinspection SpellCheckingInspection

    uitest(['aggregation'])
