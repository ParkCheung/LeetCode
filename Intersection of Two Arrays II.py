class Solution(object):

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])

        return res
# debug
nums1 = [1, 2,  3, 4]
nums2 = [1, 3, 3]

s = Solution()
print(s.intersect(nums1, nums2))
