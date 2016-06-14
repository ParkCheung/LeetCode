# coding=utf-8
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        #记录已经统计过的字符，避免重复统计
        found = []
        for i in range(len(s)):
            if s[i] in found:
                continue

            if s.count(s[i]) != t.count(s[i]):
                return False

            found.append(s[i])

        return True


s = Solution()
print(s.isAnagram("abbdda", "abbddc"))
