# 1. Palindrome Number
# https://leetcode.com/problems/palindrome number/
# Time: O(log₁₀ n), Space: O(1)


class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        num = x
        result = 0 
        while x > 0:
            ld = x % 10
            result = (result * 10) + ld
            x = x // 10
        return num == result


        
