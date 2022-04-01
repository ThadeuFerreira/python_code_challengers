# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

from typing import List

class Solution:
    # with O(1) space
    def buildArray(self, nums: List[int]) -> List[int]:
        k = 0
        while k < len(nums):
            if nums[k] > 0:
                first = nums[k]
                j = k
                while nums[j] != k and nums[j] >= 0:
                    temp = nums[j]
                    nums[j] = -nums[temp]
                    j = temp
                nums[j] = - first
            k += 1
        
        for i in range(len(nums)):
            nums[i] = -nums[i]

        return nums