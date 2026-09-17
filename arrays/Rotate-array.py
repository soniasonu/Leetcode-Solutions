#189
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        for _ in range(k):
            last = nums.pop()
            nums.insert(0, last)
