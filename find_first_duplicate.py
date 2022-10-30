# find first duplicate, return array length of found duplicate


## bruteforce
def brute_firstDuplicateValue(array):
    portioned_index = len(array)  # set this for the to get minmum array size later
    for x in range(len(array)):
        val = array[x]
        for j in range(x + 1, len(array)):
            forward_val = array[j]
            if forward_val == val:
                print('duplicate : position', val, ':', j)
                portioned_index = min(portioned_index, val)
                if portioned_index == len(array):
                    return -1
                else:
                    return portioned_index

    # return []

def firstDuplicateValue(array):
    seen = set()
    portioned_index = len(array)

    for x in range(len(array)):
        if array[x] not in seen:
            seen.add(array[x])
        elif array[x] in seen:
            print('first value', array[x])
            portioned_index = min(portioned_index, x)
            if portioned_index == len(array):
                return -1
        return array[x]





array = [2, 1, 5, 2, 3, 3, 4]
brute_results = brute_firstDuplicateValue(array)
print('brute results',brute_results)

results = firstDuplicateValue(array)
print('fast restults', results)


