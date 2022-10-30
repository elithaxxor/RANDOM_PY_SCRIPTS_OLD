class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head=Node()

    def context_manager(self, user_input, *args, **kwargs):
        if user_input == 'append':
            print('appending ll element ')
            return (self.ll_append(append_val))
        if user_input == 'length':
            print('finding ll length ')
            return self.ll_lenght()
        if user_input == 'display':
            return self.ll_display()
        if user_input == 'get position':
            return self.get_by_position(get_position)
        if user_input == 'erase position':
            return self.erase_position(erase_position)

        else:
            return f'[context-manager-msg]--> could not process {user_input}'


    def ll_append(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        if new_node:
            return f'append {new_node.data} [successfully applied]'
        else:
            return f'append {new_node.data} [fail]'


    def ll_lenght(self):
        current_node = self.head
        total_nodes = 0
        while current_node.next!=None:
            total_nodes+=1
            current_node = current_node.next
        return total_nodes

    def ll_display(self):
        print('running ll display')
        array = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            array.append(current_node.data)
        return array

    def get_by_position(self, index):
        ll_length = self.ll_lenght()
        current_index = 0
        current_node = self.head
        print('getting element by position [index] [current-length]', index ,ll_length)
        if index >= self.ll_lenght():
            return f'index [{index}] out of range [{ll_length}]--> cannot get position'
        while current_node != None:
            current_node = current_node.next
            if current_index == index:
                return f'found requested element at {current_node.data}'
            current_index += 1

    def erase_position(self, index):
        ll_lenght = self.ll_lenght()
        current_index = 0
        current_node = self.head
        if self.ll_lenght() > ll_lenght:
            return f'index [{index}] out of range [{ll_lenght}] --> cannot erase ll element'
        while current_node != None:
            prev_node = current_node
            current_node = current_node.next
            if current_index == index:
                prev_node.next = current_node.next ## rewrites the node, essenitally erasing it.
                return
            current_index += 1
            if current_index == ll_lenght:
                return f'could not erase.. '



array = [1,2,3,4,5,6,7,8,9]
append_val = 20
append_val2 = 20
get_position = 1
erase_position = 0

ll = LinkedList()
append_result = ll.context_manager('append',append_val)
append_result2 = ll.context_manager('append',append_val2)
display_results = ll.context_manager('display')
list_lenght = ll.context_manager('get length')
get_position_result = ll.context_manager('get position', get_position)
erase_position_result = ll.context_manager('erase position', erase_position)


print('X'*50)
print('[append results]', append_result)
print('[append results]', append_result2)
print('[display_results]', display_results)
print('[get by position]', get_position_result)
print('[erase by position]', get_position_result)
print('[list length]', list_lenght)
print('X'*50)
