# Solution
# Runtime: 48 ms, faster than 89.16% of Python3 online submissions for Reverse Vowels of a String.
# Memory Usage: 15.1 MB, less than 72.12% of Python3 online submissions for Reverse Vowels of a String.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        string = list(s)
        i, j = 0, len(s) - 1
        
        while i < j:
            if string[i].lower() not in vowels:
                i += 1
            elif string[j].lower() not in vowels:
                j -= 1
            else:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
        
        return ''.join(string)