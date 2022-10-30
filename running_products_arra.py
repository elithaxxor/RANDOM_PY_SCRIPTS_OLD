def arrayOfProducts(array):
    array_size = len(array)
    running_products = [1 for _ in range(array_size)]

    left_running = 1
    for x in range(array_size):  # sets array, tnen second loop multiples again
        running_products[x] = left_running  ## copys array, and creates new array for each element
        left_running *= array[x]
        # print(left_running)

    right_running = 1
    for x in reversed(range(array_size)):  ## update running_products by multiplying
        running_products[x] *= right_running
        right_running *= array[x]

    print(running_products)
    return running_products


array = [5, 1, 4, 2]
results = arrayOfProducts(array)
print(results)

