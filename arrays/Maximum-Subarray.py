#53
class Solution(object):
    def maxSubArray(self, nums):
        maxi = nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            maxi = max(maxi, current)
        return maxi
