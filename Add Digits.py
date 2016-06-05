class Solution():

    #解法1
    """
    转成字符串递归
    """
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        strn = str(num)
        while (len(strn)) > 1:
            sum = 0
            for x in strn:
                sum += int(x)
            if sum < 10:
                num = sum
                break
            else:
                num = self.addDigits(sum)
                break
        return num

    #解法2 效率更高
    """
    num = a * 10000 + b * 1000 + c * 100 + d * 10 + e 即：num = (a + b + c + d + e) + (a * 9999 + b * 999 + c * 99 + d * 9)
    因为 a * 9999 + b * 999 + c * 99 + d * 9 一定可以被9整除，因此num模除9的结果与 a + b + c + d + e 模除9的结果是一样的。
    结果不能整除为0 所以先+1 再求余
    """

    def addDigits1(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (num - 1) % 9 + 1 if num != 0 else 0;

s = Solution()
print(s.addDigits(14545))
