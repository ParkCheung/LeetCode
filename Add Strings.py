class Solution(object):

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        list1 = list(num1)
        list2 = list(num2)

        len1 = len(list1)
        len2 = len(list2)

        length = 0
        diff = len1 - len2

        if diff > 0:
            length = len1
            for x in range(0, diff):
                list2.insert(0, "0")
        else:
            length = len2
            for x in range(diff, 0):
                list1.insert(0, "0")

        res = []
        carry = 0
        for i in range(0, length):
            k = length - i - 1
            addsum = int(list2[k]) + int(list1[k]) + carry
            if addsum >= 10:
                carry = int(addsum / 10)
                addsum = addsum % 10
            else:
                carry = 0
            res.append(addsum)
        if carry > 0:
            res.append(carry)
        result = ""
        for x in res[::-1]:
            result += str(x)

        return result
s = Solution()
print(s.addStrings("408", "5"))