# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value=value
        self.next = None


    def remove_duplicates(self, value):
        linked_list = LinkedList
        print('value', value)
        print('linked list',linked_list)

        while linked_list is not None:
            next_node = self.next
            while next_node is not None and next_node.value == value:
                print(next_node)

        #     print(next_node)
        #

linked_list = [1,2,3,4,5,6,7,8]
ll = LinkedList(linked_list)
ll.remove_duplicates(ll.value)

print(ll.value)

