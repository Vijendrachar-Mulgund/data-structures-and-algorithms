# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python data structures and algorithms collection. Each data structure lives in its own directory with an implementation file and a corresponding test file (TDD approach — tests are written first).

## Environment

- Python 3.14 with a local `.venv` virtual environment
- pytest for testing
- Activate venv: `source .venv/bin/activate`

## Commands

Run all tests for a data structure:
```
python -m pytest LinkedList/ -v
```

Run a single test file:
```
python -m pytest LinkedList/test_linked_list.py -v
```

Run a specific test class or method:
```
python -m pytest LinkedList/test_linked_list.py::TestAppend -v
python -m pytest LinkedList/test_linked_list.py::TestAppend::test_append_to_empty -v
```

## Code Structure

Each data structure follows the pattern:
- `<DataStructure>/` — directory named after the data structure
- `<data_structure>.py` — implementation module
- `test_<data_structure>.py` — pytest tests, imports directly from the implementation module

Tests use relative imports (`from linked_list import Node, LinkedList`), so pytest must be run from the repo root using `python -m pytest` (not from inside the data structure directory).
