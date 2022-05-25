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
    """the node of binary tree"""
    def __init__(self, value, left=None, right=None):
        """Create a tree node with a given value.

        Args:
            x : the value of the node.
        """
        self.val = value
        self.left = left
        self.right = right


class binaryTree():
    def __init__(self,preOrder):
        self.pre = preOrder
        self.prept = 0
        self.root = self.buildTree()


    def buildTree(self): # 建立二叉树
        if self.prept >= len(self.pre):
            return None
        node = None
        if self.pre[self.prept] != '#': # 递归建树，建立左右节点后再传回
            node =TreeNode(self.pre[self.prept], self.buildTree(), self.buildTree())
        self.prept += 1 
        return node



def preOrderRecursion(root):
    """preOrder traversal of the tree using recursion.

    Args:
        root (TreeNode): the root node of the tree.
    """

    if root is None:
        return
    print(root.val, end=' ')
    preOrderRecursion(root.left)
    preOrderRecursion(root.right)


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


def inOrderRecursion(root):
    """inOrder traversal of the tree using recursion.

    Args:
        root (TreeNode): the root node of the tree.
    """
    if root is None:
        return
    inOrderRecursion(root.left)
    print(root.val, end=' ')
    inOrderRecursion(root.right)


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


def postOrderRecursion(root):
    """postOrder traversal of the tree using recursion.

    Args:
        root (TreeNode): the root node of the tree.
    """
    if root is None:
        return
    postOrderRecursion(root.left)
    postOrderRecursion(root.right)
    print(root.val, end=' ')


def postOrderNotRecursion(root):
    """postOrder traversal of the tree without recursion.

    Args:
        root (TreeNode): the root node of the tree.
    """
    if root is None:
        return
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
        print(node.val, end=' ')


def levelOrder(root):
    """levelOrder traversal of the tree using recursion.

    Args:
        root (TreeNode): the root node of the tree.
    """
    if root is None:
        return
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.val, end=' ')
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


if __name__ == '__main__':
    pre = [3,7,2,4,6,8,1]
    tree = binaryTree(pre)
    print(tree.root.val)