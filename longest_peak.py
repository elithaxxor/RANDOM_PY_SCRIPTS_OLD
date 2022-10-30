## set peak as a variabel with condtions

def longestPeak(array):
    longest_peak = 0
    check = 1
    while check < len(array) - 1:
        peak = array[check - 1] < array[check] and array[check] > array[check + 1]  # define the peak

        if not peak:
            # print('no peak at ', array[check])
            check += 1
            continue

        ## set up left and right array expansion ##
        left_index = check - 2
        while left_index >= 0 and array[left_index] < array[left_index + 1]:
            left_index -= 1

        right_index = check + 2
        while right_index < len(array) and array[right_index] < array[right_index - 1]:
            right_index += 1

        current_peak = right_index - left_index - 1
        longest_peak = max(longest_peak, current_peak)
        check = right_index
    return longest_peak


array = [34,36,67,99,88,77,66,55]
result = longestPeak(array)
print('lenght of array peak: ', result)




