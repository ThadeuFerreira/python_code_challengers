from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        finalList = []
       
        #first while loop is to find the number of combinations
        #add the first element and check if the sum is equal to the target
        #if it is, add the combination to the final list, remove two and try with the next element
        #if it is larger, remove from the list, subtract from current sum and try again
        #if it is smaller, add to the list and try again
        
        def backtracking(candidates,target, currentList, position, finalList):
            if target == 0:
                copyCurrentList = currentList.copy()
                finalList.append(copyCurrentList)
            if target < 0:
                return
            for i in range(position,len(candidates)):
                currentList.append(candidates[i])
                backtracking(candidates,target-candidates[i],currentList,i,finalList)
                currentList.pop()

        backtracking(candidates,target, [], 0,finalList)

        return finalList



s = Solution()

candidates =[2,3,5]
target = 8
print(s.combinationSum(candidates, target))

candidates = [2,3,6,7]
target = 7

print(s.combinationSum(candidates, target))

