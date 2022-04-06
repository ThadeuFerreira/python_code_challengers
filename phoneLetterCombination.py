from typing import List
from collections import Counter, heapq
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberLetterDict = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz', '0':''}

        def getCombinations(digits:str, result:str, combinations: List[str]):
            if len(digits) == 0:
                combinations.append(result)
                result = ''
                return
            chars = numberLetterDict[digits[0]]
            for i in chars:
                result += i
                getCombinations(digits[1:], result, combinations)
                result = result[:-1]
            return
        result = ''
        combinations = []
        getCombinations(digits, result, combinations)
        return combinations

    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 
s = Solution()
print(s.letterCombinations("2"))
