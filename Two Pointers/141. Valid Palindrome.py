# Soultion 1
# Time: O(n)
# Space: O(1)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        start, end = 0, len(s) - 1

        for i in range(len(s)):
            if start >= end: ## when the left pointer passes/hits the right pointer
                return True
            elif not s[start].isalnum(): ## ignore non-alphanumeric
                start += 1
            elif not s[end].isalnum(): ## ignore non-alphanumeric
                end -= 1
            elif s[start].lower() == s[end].lower(): ## if the same, move both pointers
                start += 1
                end -= 1 
            elif s[start].lower() != s[end].lower(): ## if not the same, return false
                return False
            

    
# Solution 2: Pythonic way of doing it 
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]
