from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        new_array = [1]*len(nums)
        for i in range(len(nums)):
            new_p = (i - k)%len(nums)
            new_array[i] = nums[new_p]
        return new_array 

s = Solution()


l = [1,2,3,4,5,6,7]
x = s.rotate(l,3)
print(x)