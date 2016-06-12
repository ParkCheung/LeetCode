class Solution():
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        strx = str(abs(x))
        r = int(strx[::-1])

        return sign * r if r < (1 << 31) - 1 else 0

    #debug
s = Solution()
print(s.reverse(-2147483641))
