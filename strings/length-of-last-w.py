#58
class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        pos = s.rfind(' ')
        return len(s) - pos - 1
