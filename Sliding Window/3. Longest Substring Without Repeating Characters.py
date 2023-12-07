class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0

        l, r = 0 ,1
        maxLength = 0
        while r < len(s):
            if len(s[l:r+1]) == len(set(s[l:r+1])):
                r += 1
            else:
                maxLength = max(maxLength, r-l)
                l = l + 1
                r = r + 1

        maxLength = max(maxLength, r-l)

        return maxLength

## another solution
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0

				## track the sliding window using set directly
        charSet = set()
        l = 0 
        maxLength = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLength = max(maxLength, len(charSet))
        
        return maxLength