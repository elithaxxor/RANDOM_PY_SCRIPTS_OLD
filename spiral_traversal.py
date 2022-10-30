
def spiralTraverse(array):
    results = []
    start_row, end_row = 0, len(array) - 1 # number of rows in matrix
    start_col, end_col = 0, len(array[0]) - 1
    print (array)
    print('amount of rows', start_row, end_row)
    print('amount of horizontal cells', start_col, end_col)

    while start_col <= end_col and start_row <= end_row: # condition to set up traversal, for loops dictate direction.
        for x in range (start_col, end_col + 1):  # TOP
            # print(array[x])
            # print('x'*50)
            results.append(array[start_row][x])
        for x in range (start_row +1, end_row +1):  # start_row+1 to avoid doubel counting from above for loop RIGHT
            results.append(array[x][end_col])

        for x in reversed(range(start_col, end_col)):  # BOTTOM
            if start_row == end_row:
                break
            results.append(array[end_row][x])
        for x in reversed(range(start_row +1, end_row)): # LEFT
            if start_col == end_col:
                break
            results.append(array[x][start_col])

        ### move the bounds ###
        start_row+=1
        start_col+=1
        end_row-=1
        end_col-=1
    return results




    # array = [
#     [1, 2, 3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10, 9, 8, 7]
# ]

# spiralTraverse(array)
