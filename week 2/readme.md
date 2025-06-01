Output of the code is :
![alt text](image.png)
![alt text](image-1.png)

# Linked List in Python

This project demonstrates a basic implementation of a **singly linked list** using object-oriented programming in Python. It supports adding nodes, displaying the list, and deleting nodes by position.

## Description

The program defines two main classes:

**Node**  
Represents a single element in the linked list. Each node contains:
- Data
- A reference (`next`) to the next node in the list

**LinkedList**  
Manages the linked list and provides methods to:
- Add a node to the end of the list
- Display the list
- Delete a node at a specific 1-based position

## Functionalities

- Append new nodes to the end of the list
- Print all nodes in sequence
- Delete any node by its position (with proper error checking)

## How to Use

To use the linked list:

- Create an instance of the `LinkedList` class
- Use `.append(data)` to add elements
- Use `.print_list()` to display the linked list
- Use `.delete(index)` to delete a node at the given 1-based index

These operations are demonstrated in the `__main__` block at the end of the code.

## Error Handling

The code handles various edge cases such as:

- Trying to delete from an empty list
- Providing an index less than 1
- Trying to delete a node at a position that doesn’t exist

Meaningful error messages are printed for each invalid operation.