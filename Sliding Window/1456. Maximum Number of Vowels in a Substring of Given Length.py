class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        i, j = 0, 0+k
        maxNum = 0
        cnt = 0
        for c in s[:k]:
            if c in vowels:
                cnt += 1
        
        maxNum = cnt

        for i in range(k, len(s)):
            if s[i] in vowels:
                cnt +=1
            if s[i-k] in vowels:
                cnt -= 1
            maxNum = max(maxNum, cnt)
        
        return maxNum