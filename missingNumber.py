from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        zero_index = -1
        nums.append(1)
        for i in range(len(nums) -1):
            v = abs(nums[i])
            if nums[v] == 0:
                zero_index = v
            nums[v] = -abs(nums[v])
        nums[zero_index] = -1
        for i in range(len(nums)):
            if nums[i] >= 0 :
                return i
        return len(nums)

s = Solution()
print(s.missingNumber([2,0]))
print(s.missingNumber([0,1,3]))
n = [9,6,4,2,3,5,7,0,1]
print(s.missingNumber(n))