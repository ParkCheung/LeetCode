# coding=utf-8
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        count = 0
        offset = 0
        for i in range(0, size):
            if nums[i] != 0:
                nums[offset], nums[offset + count] = nums[offset + count], nums[offset]
                offset += 1
            else:
                count += 1

            if offset + count > size:
                break

        #提交时不需要return
        return nums


s = Solution()
print(s.moveZeroes([1, 0, 1, 0, 3, 12]))
