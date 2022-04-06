class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        longest = 1
        i = 0
        j = 1
        rep = {}
        rep[s[0]] = 0
        while j < len(s):
            if s[j] in rep:
                i = rep[s[j]] + 1
                #remove values from the dictionary smaller than i
                temp = {}
                for k in rep:
                    if rep[k] >= i:
                        temp[k] = rep[k]
                rep = temp
            longest = max(longest, j-i+1)
            rep[s[j]] = j
            j += 1
        return longest

s = Solution()
print(s.lengthOfLongestSubstring("abba"))
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("asdfgh"))