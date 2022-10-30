from random import randint

''' quicksort in place '''
def create_array(size = 20, max=50):
    return [randint(0, max) for _ in range(size)]


def partition_array(array, low, high):
    i = low-1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i+=1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i+1]
    return i+1

def quick_sort(array, low=0, high=None):
    if high == None:
        high = len(array)-1
    if low < high:
        p_index = partition_array(array, low, high) ## divies up partitions
        quick_sort(array, low, p_index-1)
        quick_sort(array, p_index+1, high)
    return array
rand_array = create_array()
sorted_array=quick_sort(rand_array)
print(rand_array)
print(sorted_array)
