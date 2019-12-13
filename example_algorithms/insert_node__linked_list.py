import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# my code
def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    node = head
    # traverse until position
    for x in range(position):
        actual = node
        siguiente = actual.next
        node = siguiente

    # insert new_node next to actual
    actual.next = new_node
    # next of new_node is siguiente
    new_node.next = siguiente
    return head

