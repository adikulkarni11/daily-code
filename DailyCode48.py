"""This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]
And the following inorder traversal:

[d, b, e, a, f, c, g]
You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g"""

# Aditya Kulkarni
## Dec 6 2020
### Implemented with the help of leetcode.com https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# ----------------


# lets build a binary tree class
from collections import *
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = deque(preorder)
        return self.help(preorder, inorder)

    def help(self, preorder, inorder):
        if inorder:
            index = inorder.index(preorder.popleft())
            node = TreeNode(inorder[index])
            node.left = self.help(preorder, inorder[:index])
            node.right = self.help(preorder, inorder[index+1:])
            return node
 
 """Accepted
Runtime: 36 ms
Your input
[3,9,20,15,7]
[9,3,15,20,7]
Output
[3,9,20,null,null,15,7]
Expected
[3,9,20,null,null,15,7]"""