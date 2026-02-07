# Data Structures and Algorithms

A collection of classic data structures and algorithms implemented in Python, built using a test-driven development (TDD) approach.

## Project Structure

Each data structure lives in its own directory with an implementation file and a corresponding test file:

```
<DataStructure>/
├── <data_structure>.py          # Implementation
└── test_<data_structure>.py     # Tests
```

## Implemented Data Structures

### Linked List

A singly linked list implementation with the following operations:

| Method       | Description                                      |
|--------------|--------------------------------------------------|
| `append`     | Add a node to the end of the list                |
| `prepend`    | Add a node to the beginning of the list          |
| `pop`        | Remove and return the last node                  |
| `pop_first`  | Remove and return the first node                 |
| `get`        | Retrieve the node at a given index               |
| `set_value`  | Update the value of the node at a given index    |
| `insert`     | Insert a new node at a given index               |
| `remove`     | Remove the node at a given index                 |
| `print_list` | Print all node values in order                   |

## Getting Started

### Prerequisites

- Python 3.14+

### Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running Tests

Run all tests for a specific data structure:

```bash
python -m pytest LinkedList/ -v
```

Run a single test file:

```bash
python -m pytest LinkedList/test_linked_list.py -v
```

Run a specific test class or method:

```bash
python -m pytest LinkedList/test_linked_list.py::TestAppend -v
python -m pytest LinkedList/test_linked_list.py::TestAppend::test_append_to_empty -v
```
