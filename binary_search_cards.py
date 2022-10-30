def locate_card(array, query):
    start_index = 0
    while start_index <= len(array):
        if array[start_index] == query:
            return array[start_index]
        start_index+=1
    return -1

def locate_card_ii(array, query):
    def condition(mid):
        if array[mid] == query:
            return 'found'
        elif array[mid] <= query:
            return 'left'


    low, high = 0, len(array)
    while low <= high:
        mid = (low + high) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        elif result:
            low = mid + 1
    return -1

def condition()



array = [4,5,2,1,2,4,5,6,23]
query = 1
results= locate_card_ii(array, query)
print(results)

# for x in range(len(array)):
#     mid_val = array[mid]
#     for y in range(len(array)):
#         if mid_val != query:
#             array[mid] = array[high - 1]
#             array[mid] = array[low + 1]
#         if query == array[mid]:
#             return array[mid]
#