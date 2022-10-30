## funciton taht takes in a non empty array of intagers (target)
# if any two element in the array sum up to the target, then then return val
# o(n) -- hash tables


def main():
    target_sum = 9
    input_array = [1,2,3,4,5,12,52,35]

    def twoNumbersSum(array, targetSum):
        nums = {} # initilize hash table
        for num in array:
            possible_match = targetSum - num

            if possible_match in nums:
                return[possible_match, num]

            else:
                nums[num]=True ## store current # in hash table

        return[]

    twoNumbersSum(input_array, target_sum) # call function

if __name__ == '__main__':
    rv = main()
    print(rv)

