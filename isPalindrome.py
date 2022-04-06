from operator import truediv


class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove all spaces and non-alphanumeric characters and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

s = Solution()
print(s.isPalindrome("abba"))
print(s.isPalindrome("abeba"))
print(s.isPalindrome("abcabcbb zxczxczxc"))
print(s.isPalindrome("A man, a plan, a canal: Panama"))
