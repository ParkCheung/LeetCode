class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        for i in range(size):
            for j in range(i):
                if nums[j] == nums[i]:
                    return True
        return False
# debug

s = Solution()
print(s.containsDuplicate([2, 1]))
