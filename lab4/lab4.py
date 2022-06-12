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
    def __init__(self, x, left=None, right=None):
        """Create a tree node with a given value.

        Args:
            x : the value of the node.
        """
        self.val = x
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None  # 初始化时根节点为None
        self.queue = [] 
    def add(self,item):
        """Add a node to the tree.
        
        Args:
            item : the value of the node.
        """
        node = TreeNode(item)
        if self.root is None:# if the tree is empty, the root is the new node
            self.root = node
            return 
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                # if the left child is empty, add the new node to the left child
                cur_node.left = node
                return
            else:
                # if the left child is not empty, add the new node to the right child
                queue.append(cur_node.left)
            
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)


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

def postOrder_recursion(root):
    """postOrder traversal of the tree using recursion.

    Args:
        root (TreeNode): the root node of the tree.
    """
    if root is None:
        return
    postOrder_recursion(root.left)
    postOrder_recursion(root.right)
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
    pre = [5,3,7,2,4,6,8,1]
    tree = Tree()
    tree.root = TreeNode(pre[0])
    for i in range(1, len(pre)):
        tree.add(pre[i])
    print('preOrder traversal of the tree using recursion:')
    preOrder_recursion(tree.root)
    print('\npreOrder traversal of the tree without recursion:')
    preOrderNotRecursion(tree.root)
    print('\ninOrder traversal of the tree using recursion:')
    inOrder_recursion(tree.root)
    print('\ninOrder traversal of the tree without recursion:')
    inOrderNotRecursion(tree.root)
    print('\npostOrder traversal of the tree using recursion:')
    postOrder_recursion(tree.root)
    print('\npostOrder traversal of the tree without recursion:')
    postOrderNotRecursion(tree.root)
    print('\nlevelOrder traversal of the tree using recursion:')
    levelOrder(tree.root)