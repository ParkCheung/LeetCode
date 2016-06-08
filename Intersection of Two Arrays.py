class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if len(nums1) != 0 and len(nums2) != 0:
            res = list(set(nums1).intersection(set(nums2)))
        return res

#debug
nums1 = [1,2,3,4]
nums2 = [1,3]

s = Solution();
print(s.intersection(nums1,nums2))