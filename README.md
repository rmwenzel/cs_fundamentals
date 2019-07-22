# CS Fundamentals
---

OOP implementations of fundamental data structures and algorithms in Python 3.


## Overview

This is a personal project for learning purposes. The main aims are:

- Learn data structures and algorithms through scratch implementations
- Practice object-oriented programming
- Practice good software development:
	- documentation
	- version control
	- unit testing
	- virtual environment

Development is ongoing


## `structures/`

This directory contains implementations of various famous abstract data types. Implemented so far are:

- `nodes.py` - Node types
	- `SingleNode` - Node with single pointer
	- `DoubleNode` - Node with two pointers

- `linkedlist.py` - Linked-list types
	- `SinglyLinkedList` - Singly-linked lists





## Requirements 

Although there are few packages beyond the python standard library, I'm using a 
[conda virtual environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#). The file 'environment.yml' contains all conda and pip dependencies. If you have conda installed you can create the environment with

```
conda env create -f environment.yml
```

## Testing
These are in the tests directory. Tests use pytest and can be run from the root directory.

```
python -m pytest
```
