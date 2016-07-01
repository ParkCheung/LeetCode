class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        dictionary = {}
        for num in nums1:
            if not num in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        for num in nums2:
            if num in dictionary and dictionary[num] > 0:
                dictionary[num] -= 1
                res.append(num)
        return res;

s = Solution()
print(s.intersect([1, 3, 3], [1, 3]))

