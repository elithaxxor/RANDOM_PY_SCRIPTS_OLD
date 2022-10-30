nums = [1,2,3]
i_nums = iter(nums)
#
print(type(i_nums))
print(i_nums)
print(dir(i_nums))


#

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current
#

penis = MyRange (1, 1099999999)
print(penis)

for num in nums:
    num = MyRange (1,1099999999)
    print(MyRange)


#
