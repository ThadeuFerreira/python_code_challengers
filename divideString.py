class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        max_s = str1
        min_s = str2
        if len(min_s) > len(max_s):
            min_s, max_s = max_s, min_s
        
        start = 1
        result = ''
        hasSub = False
        i = 0
        while start + len(min_s) -1 < len(max_s):
            i = 0
            while i < len(min_s) and max_s[start+i] == min_s[i]:
                i += 1
            if i == len(min_s):
                hasSub = True
                break
            start += 1
        if hasSub:
            for i in range(len(max_s)):
                if i < start or i > start + len(min_s) -1:
                    result += max_s[i]
        return result

s = Solution()
s1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
s2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
print(s.gcdOfStrings(s1, s2))
print(s.gcdOfStrings("ABCABC", "ABC"))
