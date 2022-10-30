def insertionSort():

    def swap(i, j, array):
        ''' nested function sort through array elements/vals '''
        array[i], array[j] = array[j], array[i]
        print(array)



    array = [1, 14 ,8, 5,6 , 20 ,9,32]
    print(array)
    for i in range(1, len(array)):
        j = i
        j_step = j-1
        while j > 0 and array[j] < j_step:
            swap(i, j, array)
            j -= 1


def main():
    insertionSort()

if __name__ == '__main__':
    main()
