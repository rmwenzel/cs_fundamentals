OOP implementations of fundamental data structures and algorithms in Python 3.


## Overview

This is a personal project for learning purposes. The main aims are:

- Learn data structures and algorithms through scratch implementations
- Practice object-oriented programming
- Practice good software development:
	- documentation
	- version control
	- unit testing

## Data Structures

Implementations of various standard abstract data types. These are in found in the `structures/` directory. Implemented so far are:

- `linkedlist.py`
	- `SinglyLinkedList`

- `tree.py`
	- `BinarySearchTree`

- `graph.py`
	- `DirGraph` - directed graph
	- `Graph` - undirected graph

## Algorithms

Implementations of various standard algorithms. These are in found in the `algorithms/` directory. Implemented so far are:


- `mult.py`
	- `recmult` - naive recursive multiplication
	- `karutsaba` - Karutsaba multiplication

- `listsort.py`
	- `ListSort` - Built-in `list` class augmented with sort methods
		- `.quicksort`
		- `.mergesort`

- `graphprocess.py`
	- `DirGraphProcess` - `stuctures.DirGraph` augmented with graph processing methods
		- `dfs_rec_shortpath` - Recursive depth-first search for shortest path
		- `dfs_it_shortpath` - Iterative depth-first search for shortest path
		- `bfs_it_shortpath` - Iterative breadth-first search for shortest path
		- `dfs_rec_traversal` - Recursive depth-first traversal
		- `dfs_it_shortpath` - Iterative depth-first traversal



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

