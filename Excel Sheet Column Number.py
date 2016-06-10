class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        size = len(s)
        for i,ch in enumerate(s):
        	res += (ord(ch)-64) * 26**(size - i - 1)
        	
       	return res
s = Solution()
print(s.titleToNumber("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"))