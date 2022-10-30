def spiralTraverse(array):
    results = []
    start_row, end_row = 0, len(array) - 1 # number of rows in matrix
    start_col, end_col = 0, len(array[0]) - 1
    print (array)
    print('amount of rows', start_row, end_row)
    print('amount of horizontal cells', start_col, end_col)

    count=0
    while start_col <= end_col and start_row <= end_row: # traverse top
        print(array[count])
        print('x'*50)
        count+=1
        for x in range (start_row, end_row+1):
            print(array[x])

    # count2=0
    # while start_row <= end_row:
    #     print(array[count2])
    #     print('x'*50)
    #     count2+=1
    # while end_row <= start_row:
    #     print(array[count2])



array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7],
]

spiralTraverse(array)

