# CS Fundamentals
---

OOP implementations of fundamental data structures and algorithms in Python 3.


## Overview

This is a personal project for learning purposes. The main aims are:

- Learn data structures and algorithms through scratch implentations
- Practice object-oriented programming
- Practice good software development:
	- documentation
	- version control
	- unit testing
	- virtual environment

Development is ongoing

## Data Structures

These are in the `structs` directory. Implemented so far are

- Linked list structures (`linkedlist.py`):
	- `SinglyLinkedList`

## Requirements 

Package dependencies are in `environment.yml`, a
[conda virtual environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) config file. If you have conda installed you can create the environment with

```
conda env create -f environment.yml
```

## Testing

These are in the `tests` directory. Tests use `pytest` and can be run from the root directory.

```
python -m pytest
```

