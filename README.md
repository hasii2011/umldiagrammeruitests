[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/hasii2011/umldiagrammeruitests/graphs/commit-activity)
[![PyPI version](https://badge.fury.io/py/umldiagrammeruitests.svg)](https://badge.fury.io/py/umldiagrammeruitests)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Copilot: No](https://img.shields.io/badge/GitHub_Copilot-No-red?logo=github&style=flat-square)](https://github.com/hasii2011/code-ally-basic/wiki/GitHub-Copilot)

# UI Test Automation Suite

This project contains a suite of UI automation tests for the UML Diagrammer application. These tests use the `pyautogui` library to simulate user interactions and verify the correctness of the application's behavior.

## Documentation

* 📖 [Read UI Test Suite Description (Markdown)](developer/TestDescription.md)
* 📄 [View UI Test Suite Description (PDF)](developer/TestDescription.pdf)
* 📝 [Download editable Word Document (.docx)](developer/TestDescription.docx)

## Test CLI

Currently, this project supports the following tests:

```
Usage: uitest [OPTIONS] COMMAND [ARGS]...

  The UML Diagrammer UI Test driver

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  aggregation  Execute the create an aggregation relationship test
  basicClass   Execute the test for basic class creation
  composition  Execute the create a composition relationship test
  inheritance  Execute the create an inheritance relationship test
  interface    Execute the create an implement interface test
  noteLink     Execute the create a Uml Note link relationship test
  
```

## Utility Scripts

- **`gists/FixIDRegExTest.py`**: A small utility script for testing and debugging the regular expression used to remove unique IDs from the generated XML files during the comparison process.
- **`TrackMouse.py`**: A simple script that prints the current mouse coordinates to the console. This is useful for finding the screen coordinates needed for the `pyautogui` test scripts.

## Running the Tests

To run these tests, you need to have the UML Diagrammer application running. Then, you can execute each test from your terminal. For example:

```bash
# Run a specific UI test
uitest aggregation
uitest basicClass
uitest composition
uitest inheritance
uitest interface
uitest noteLink
```

**Prerequisites**

The debug section in `umlDiagrammer.ini` must use the following values:

```ini
[Debug]
inTestMode = True
testPosition = 20,40
testSize = 1247,950
```

# Installation

```bash
pip install umldiagrammeruitests
```

___

Written by <a href="mailto:humberto.a.sanchez.ii@gmail.com?subject=Hello Humberto">Humberto A. Sanchez II</a>  (C) 2026

## Note
For all kinds of problems, requests, enhancements, bug reports, etc., please drop me an e-mail.

------
> [!NOTE]
> **I do not consent to GitHub's use of this project's code in Copilot.** See our [GitHub Copilot Statement](https://github.com/hasii2011/code-ally-basic/wiki/GitHub-Copilot) for details.

