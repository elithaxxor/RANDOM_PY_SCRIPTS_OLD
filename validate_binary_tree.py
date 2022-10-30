# This is an input class. Do not edit.
# left elements has to be smaller than the right node and parent
# right elements have to be larger than left elements and parent

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        #print(self.value)

def validateBst(node):
    return helper_function(node, float('-inf'), float('inf'))

def helper_function(node, min_val, max_val):
    if node is None:
        return True
    elif node.value < min_val or node.value > max_val:
        return False
    left_validate = validateBst(node.right, min_val, node.value)
    return left_validate and helper_function(node.right, node.value, max_val)


# value = [[23,41,3252,6346,436,3463,63463,346,346,4363,34,436,643,63],23]\
value = {
    "nodes": [
        {"id": "1", "left": "2", "right": "3", "value": 1},
        {"id": "2", "left": "4", "right": "5", "value": 2},
        {"id": "3", "left": "6", "right": "7", "value": 3},
        {"id": "4", "left": "8", "right": "9", "value": 4},
        {"id": "5", "left": None, "right": None, "value": 5},
        {"id": "6", "left": None, "right": None, "value": 6},
        {"id": "7", "left": None, "right": None, "value": 7},
        {"id": "8", "left": None, "right": None, "value": 8},
        {"id": "9", "left": None, "right": None, "value": 9}
    ],
    "root": "1"
}


b = BST(value)
#print(b.value)
validateBst(b.value)


