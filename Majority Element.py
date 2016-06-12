class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 1:
            return nums[0]
        half = size / 2

        for num in set(nums):
            if nums.count(num) > half:
                return num


s = Solution()
print(s.majorityElement([1, 2, 1, 1, 2]))