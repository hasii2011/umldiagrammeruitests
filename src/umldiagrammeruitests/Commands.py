
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

from umldiagrammeruitests._version import __version__
from umldiagrammeruitests.verifiers.AggregationVerifier import AggregationVerifier
from umldiagrammeruitests.verifiers.BasicClassVerifier import BasicClassVerifier
from umldiagrammeruitests.verifiers.CompositionVerifier import CompositionVerifier
from umldiagrammeruitests.verifiers.InheritanceVerifier import InheritanceVerifier

from umldiagrammeruitests.Common import PAUSE_AFTER_EACH_CALL

from umldiagrammeruitests.verifiers.Environment import Environment

RESOURCES_PACKAGE_NAME:       str = 'umldiagrammeruitests.resources'
JSON_LOGGING_CONFIG_FILENAME: str = 'loggingConfiguration.json'


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
    The UML Diagrammer UI Test driver
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
    Execute the create an inheritance relationship test
    """
    secho(f'{environment}')     # temp until we start using it
    inheritanceVerifier: InheritanceVerifier = InheritanceVerifier()
    inheritanceVerifier.execute()


@uitest.command(name='composition')
@pass_obj
@handleUiTestErrors
def composition(environment: Environment):
    """
    Execute the create a composition relationship test
    """
    secho(f'{environment}')     # temp until we start using it
    compositionVerifier: CompositionVerifier = CompositionVerifier()
    compositionVerifier.execute()

@uitest.command(name='aggregation')
@pass_obj
@handleUiTestErrors
def aggregation(environment: Environment):
    """
    Execute the create an aggregation relationship test
    """
    secho(f'{environment}')     # temp until we start using it
    aggregationVerifier: AggregationVerifier = AggregationVerifier()
    aggregationVerifier.execute()


@uitest.command(name='basicClass')
@pass_obj
@handleUiTestErrors
def basicClass(environment: Environment):
    """
    Execute the a test for basic class creation
    """
    secho(f'{environment}')     # temp until we start using it
    basicClassVerifier: BasicClassVerifier = BasicClassVerifier()
    basicClassVerifier.execute()


if __name__ == '__main__':
    # noinspection SpellCheckingInspection

    uitest(['aggregation'])
