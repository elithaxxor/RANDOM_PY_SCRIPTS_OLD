''' RETURN THE MAX AMOUNT OF TRAVERSALS IN A VECTOR '''

def number_of_traversals_slow(width, height):
    height = int(height)
    width = int(width)
    if int(width) == 1 or int(height) == 1:
        print(f'not much to do..[lxw] {width}, " :: ", {height}' )
        return 1
    return number_of_traversals_slow(width-1, height) + number_of_traversals_slow(width, height-1)

def number_of_traversals_fast(width, height):
    ''' CREATE EMPTY 2D ARRAY, THEN STORE POSSIBLE VAL FROM LOOP '''
    x_axis = width +1
    y_axis = height + 1
    start = 1
    empty_array = [[0 for _ in range(x_axis) for _ in range(y_axis)]]
    y_end, x_end = max(0, y_axis), max(0, y_axis)
    print('empty array', empty_array)
    print('x axis:', x_axis, 'y axis', y_axis)
    print('x len:', x_end, 'y end', y_end)

    count_x, count_y = 0, 0
    for x in range(start, x_axis):
        count_x+=1
        for y in range(start, y_axis+1):
            print('col',x,'row',y)
            count_y+=1
            if int(x) == 1 or int(y) == 1:
                ''' IF ARRAY LAYS ON Y OR X AXIS, IT WILL AUTO FILL with # OF POSSIBLITY (1)'''
                empty_array[x][y] = count_x, count_y
                #print('filled edghes', empty_array[x][y])
            else:
                ''' fill let and up info'''
                left = empty_array[y][x-1]
                up = empty_array[y-1][x]

                if (x == x_end-1) or (y == y_end-1):
                    return f'[LEFT]{left}[UP]{up}[ARRAY]{empty_array}'



def main():
    w, h = 4,3
    results = number_of_traversals_slow(w, h)
    fast_results = number_of_traversals_fast(w, h)
    print('slow results',results)
    print('fast results',fast_results)

if  __name__ == '__main__':
    main()


