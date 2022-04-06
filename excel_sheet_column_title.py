class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        L = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        v = columnNumber
        s = []
        while v > 0:
            v = v - 1
            s.append(L[v%26])
            v = v // 26
        return ''.join(reversed(s))

s = Solution()
#should return ZY
print(s.convertToTitle(701))
#should return A
print(s.convertToTitle(1))
#should return AB
print(s.convertToTitle(28))



