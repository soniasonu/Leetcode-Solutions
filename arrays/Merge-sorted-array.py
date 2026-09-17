#88
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        arr = []
        for i in range(m):
            arr.append(nums1[i])
        for j in range(n):
            arr.append(nums2[j])
        arr.sort()
        for i in range(m+n):
            nums1[i] = arr[i]
            
