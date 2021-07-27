# Solution 1
# Runtime: 1228 ms, faster than 51.58% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.3 MB, less than 62.35% of Python3 online submissions for Longest Palindromic Substring.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        i, j = 0, 0
        while j < len(s):
            left, right = i, j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > end - start:
                    start, end = left, right
                left -= 1
                right += 1
            if i == j:
                j += 1
            else:
                i += 1
        return s[start: end+1]
    

# Solution 2
# Runtime: 944 ms, faster than 81.09% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.4 MB, less than 62.35% of Python3 online submissions for Longest Palindromic Substring.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""
        
        for i in range(len(s)):
            substr = self.getLongestPalindrome(s, i, i)
            if len(substr) > len(palindrome):
                palindrome = substr
            
            if i+1 < len(s):
                substr = self.getLongestPalindrome(s, i, i+1)
                if len(substr) > len(palindrome):
                    palindrome = substr
        
        return palindrome
            
    def getLongestPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]
        
        