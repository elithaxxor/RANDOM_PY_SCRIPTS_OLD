from random import randint

def quick_sort(array):
    print('sorting..', array)
    if len(array) < 1:
        return f'array is too small [{len(array)}]'
    smaller, equal, larger = [],[],[]
    pivot = array[randint(0, len(array)-1)]
    print('pivoting at.. ',pivot)

    for x in array:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quick_sort(smaller) + equal + quick_sort(larger)

array = [4,5,3,2,3,7,56,345,6,34,5,6]
result = quick_sort(array)
print(result)