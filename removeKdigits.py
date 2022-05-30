# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        length = len(num)
        if length == k:
            return "0"
        num = list(num)
        for i in range(k):
            n1 = 0
            n2 = 1
            while n1 < length and n2 < length and num[n1] <= num[n2]:
                n1 += 1
                n2 += 1
            if n1 < length:
                num.pop(n1)
        if length == 0:
            return "0"
        num = ''.join(num)
        v = int(num)
        return str(v)