class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.fun(n, [])

    def fun(self, n, found):
        sum = 0
        for x in str(n).replace('0', ''):
            sum += int(x) ** 2

        if sum == 1:
            return True
        else:
            if sum in found:
                return False
            found.append(sum)

            return self.fun(sum, found)
