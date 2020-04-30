class FirstUnique:

    def __init__(self, nums: List[int]):
        self.set = set()
        self.dict = collections.OrderedDict()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        return next(iter(self.dict.keys()), -1)

    def add(self, value: int) -> None:
        if value in self.set:
            self.dict.pop(value, None)
        else:
            self.dict[value] = 1
            self.set.add(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
