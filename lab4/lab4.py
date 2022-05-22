#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   lab4.py
@Time    :   2022/05/22 08:47:22
@Author  :   Tianyi Wang
@Version :   1.0
@Contact :   tianyiwang58@gmail.com
@Desc    :   None
'''

# here put the import lib


class TreeNode():
    def __init__(self, x):
        """Create a tree node with a given value.

        Args:
            x : the value of the node.
        """
        self.val = x
        self.left = None
        self.right = None


class Tree():
    def __init__(self, root):
        """Create a tree with a given root node.

        Args:
            root (TreeNode): the root node of the tree.
        """
        self.root = root

    def insert(self, node, val):
        """Insert a new node with a given value to the tree.

        Args:
            node (TreeNode): the node to insert.
            val (int): the value of the node.
        """
        if node.val > val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self.insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self.insert(node.right, val)

    def print_tree(self, node):
        """Print the tree in a level order traversal.

        Args:
            node (TreeNode): the root node of the tree.
        """
        if node is None:
            return
        queue = [node]
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.val, end=' ')
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print()

    def search(self, node, val):
        """Search for a node with a given value.

        Args:
            node (TreeNode): the root node of the tree.
            val (int): the value of the node.
        """
        if node is None:
            return False
        if node.val == val:
            return True
        if node.val > val:
            return self.search(node.left, val)
        else:
            return self.search(node.right, val)

    def delete(self, node, val):
        """Delete a node with a given value.

        Args:
            node (TreeNode): the root node of the tree.
            val (int): the value of the node.
        """
        if node is None:
            return
        if node.val == val:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                node.val = self.find_min(node.right)
        elif node.val > val:
            self.delete(node.left, val)
        else:
            self.delete(node.right, val)


def preOrder_recursion(root):
    """preOrder traversal of the tree using recursion.

    Args:
        root (TreeNode): the root node of the tree.
    """

    if root is None:
        return
    print(root.val, end=' ')
    preOrder_recursion(root.left)
    preOrder_recursion(root.right)


def preOrderNotRecursion(root):
    """preOrder traversal of the tree without recursion.

    Args:
        root (TreeNode): the root node of the tree.
    """
    if root is None:
        return
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        print(node.val, end=' ')
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)


def inOrder_recursion(root):
    """inOrder traversal of the tree using recursion.

    Args:
        root (TreeNode): the root node of the tree.
    """
    if root is None:
        return
    inOrder_recursion(root.left)
    print(root.val, end=' ')
    inOrder_recursion(root.right)


def inOrderNotRecursion(root):
    """inOrder traversal of the tree without recursion.

    Args:
        root (TreeNode): the root node of the tree.
    """
    if root is None:
        return
    stack = []
    while len(stack) > 0 or root is not None:
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.val, end=' ')
            root = root.right
