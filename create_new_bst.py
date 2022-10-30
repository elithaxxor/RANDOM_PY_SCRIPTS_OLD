''' o(log)n --> average. [if tree is balanced] '''

''' NODES--> INPUT VAL AND L/R '''
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        print('value from Node class', self.value)



''' ROOT NODE '''
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        self.count = 0

        print('self.root', self.root)

    ''' To Display Root Nodes and Input Vals '''
    def show_root_nodes(self, *args, **kwargs):
        root_node = self.root.value
        print('[INSERTION VAL]', insertion)
        print(f'[SEARCHING]--> {search}')
        print(f'[ROOT-NODE]--> {root_node}')
        print(f'[LEFT-NODE]-->  {self.root.left.value}')
        print(f'[RIGHT-NODE]--> {self.root.right.value}')

    ''' context manager for user input '''
    def tree_function(self, traversal_type, **kwargs):
        if traversal_type == 'make array':
            print('makig array.. ')
            return self.make_array
        if traversal_type == 'validate':
            print('starting BST validation [root]', bt.root.value)
            return self.validate_tree(bt.root)
        if traversal_type == 'preorder':
            print('starting preorder [root]', bt.root.value)
            return self.pre_order_traversal(bt.root, "")
        if traversal_type == 'inorder':
            return self.in_order_traversal(bt.root, "")
        if traversal_type == 'insert':
            return self.tree_insert(bt.root, insertion)
        if traversal_type == 'search':
            return self.tree_search(bt.root, search)

        if traversal_type == 'min height':
            return self.tree_min_height(bt.root, "")
        else:
            return f"{False} could not find {traversal_type} method call"

    def make_array(self, array_size=100, max_int=1000):
        from random import randint
        for _ in range(array_size):
            current_index = randint(0, max_int)
            self.tree_insert(1, current_index)



    ######### ######### #########   BST LOGIC ######## ############## ######## ######
    def validate_tree(self, node, *args):
        ''' function to compare min-max to infinity. left compare to max. right node compare to min'''
        def validate_nodes(node, min, max):
            ''' to validate, left must be less than root && left leaf. right must be more than root && more than parent leaf '''
            print('[VALIDATING BINARY-TREE]')
            if node is None:
                return f'{True} node is none, therefore [true]'
            if node.value < min or node.value >= max:
                return False
            left_isValid = validate_nodes(node.left, min, node.value)
            return left_isValid and validate_nodes(node.right, node.value, max)
        return validate_nodes(node, float('-inf'), float('inf'))

    def pre_order_traversal(self, node, traversal):
        ''' root to left to right'''
        if node:
            traversal += (str(node.value) + "-")
            traversal = self.pre_order_traversal(node.left, traversal)
            traversal = self.pre_order_traversal(node.right, traversal)
          #  count = count + 1
       # print('pre_order_traversal count: ', count)
        return traversal


    def in_order_traversal(self, node, traversal):
        count = self.count
        ''' left, root, right '''
        if node:
            traversal = self.in_order_traversal(node.left, traversal)
            traversal += f"{node.value} || "
            traversal = self.in_order_traversal(node.right, traversal)
            #count += 1
        return traversal

    def tree_insert(self, node, insertion):
        current_node = self.root.value
        print(current_node)
        print(insertion)
        while True:
            if insertion < current_node:
                break
            else:
                ### TEST BOTH OF THEM ###
                #current_node = insertion
                current_node = insertion
            if node is None:
                current_node = insertion
                break
            else:
                current_node = insertion
            return current_node

    def tree_search(self, node, search_val):
        root_node = self.root.value
        ##left_node = self.root.left.value
        ##right_node = self.root.right.value
       # bt.show_root_nodes(self)
        print(f'[SEARCHING]--> {search_val}')
        if search_val < root_node:
            if self.root.left.value is None:
                return f'could not find {search_val}, left node is {self.root.left.value}'
            else:
                return self.tree_search(self, self.root.left.value)

        elif search_val > root_node:
            if self.root.right.value is None:
                return f'could not find {search_val}, right node is {self.root.right.value}'
            else:
                return self.tree_search(self, self.root.right.value)
        else:
            return f'found val {root_node} {self.root.value} node'

    def tree_min_height(self, node, next_node):
        bt.show_root_nodes()

        print(node.value)
        print(next_node)
        def construct_min_height(array, bst, start_index, end_index):
            pass
        pass

''' TREE SETUP '''

bt = BinaryTree(1) ## ROOT
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)
bt.root.left.left.left = Node(8)
bt.root.left.right.right = Node(9)
bt.root.right.left.right = Node(10)
bt.root.right.right.left = Node(11)


new_array = bt.make_array()
print('new_array',new_array)

''' KWARG FOR METHOD CALL '''
insertion = 10
search = 5
''' METHOD CALLS '''
pre_order_result = bt.tree_function("preorder")
in_order_results = bt.tree_function('inorder')
insert_results = bt.tree_function("insert")
insert_results2 = bt.tree_function('inorder')
#search_results = bt.tree_function('search')
validate_bst = bt.tree_function('validate')
tree_min_height = bt.tree_function('min height')
''' RENDER RESULTS '''
print('pre order results ', pre_order_result, 'COUNT')
print('in order results ', in_order_results)
print('insert results ', insert_results)
print('insert results2 ', insert_results2)
#print('search results ', search_results)
print('valid_BST?', validate_bst)
print('min height?', tree_min_height)

node = BinaryTree(20)
print('node run',node)


# #
# ''' LEFT '''
# for left in left_value:
#     bt.root.left(left)
#
# ''' RIGHT '''
# for right in right_value:
#     bt.root.right(right)

#print(bt.root.left)
# for x in value:
# #     bt = BinaryTree(x)
#
# left_value = [143, 525, 234, 423 , 4234, 4324 ,43,4234,4,234,234]
# right_value = [13, 52, 34, 42 , 424, 44 ,43,434,4,4,2]