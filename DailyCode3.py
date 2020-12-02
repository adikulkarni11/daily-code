"""Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree."""

"""
This test case should pass
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def s_helper(node, Fstring):
    # Go through the tree. First root, then left subtree, then right. For all None nodes, I am appending a * for a place holder.

    if node == None:                          # If node is empty
        #print("yer")
        Fstring += "* "                       # Put a *
        return Fstring

                                              # If node has value
    Fstring += node.val + " "            # Put val in.
    #print(Fstring)
    Fstring = s_helper(node.left, Fstring)
    Fstring = s_helper(node.right, Fstring)
    #print(Fstring)
    return Fstring

def serialize(root):
    return s_helper(root, " ")

print("Serialized String =", serialize(Node('root', Node('left', Node('left.left')), Node('right'))),"")
#print(s_helper(Node('root', Node('left', Node('left.left')), Node('right')),""))

def deserialize(yerString):
    if yerString:
        yerList = yerString.split(" ")
        yerrList = yerList[1:-1]            # Taking spaces out
        yerIter = iter(yerrList)
        
        def putValue(iter_vals):            # Iterate through the list of string items
            yer = next(iter_vals)
            if yer == "*":
                return None
            else:
                node = Node(yer)
                node.left = putValue(iter_vals)
                node.right = putValue(iter_vals)

                return node
        return putValue(yerIter)

    else:
        return None

print("\n")
print(deserialize(serialize(Node('root', Node('left', Node('left.left')), Node('right')))))
node = Node('root', Node('left', Node('left.left')), Node('right'))
print("Assert: ",deserialize(serialize(node)).left.left.val == 'left.left')
