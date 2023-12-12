class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        listLen = len(words)
        wordLen = len(words[0])
        window = listLen * wordLen

        result = []

        for i in range(len(s)):
            if len(s) < i + window:
                break
            
            substr = s[i:i+window]
            substrList = [substr[n:n+wordLen] for n in range(0, len(substr), wordLen)]

            if sorted(substrList) == sorted(words):
                result.append(i)

        return result