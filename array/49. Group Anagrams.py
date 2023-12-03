## Solution 1: with sorting
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        if len(strs) == 1:
            return [strs]
        
        res = dict()
        for s in strs:
            key = ''.join(sorted(s))

            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
                
        return list(res.values())


## Solution 2: without sorting
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        if len(strs) == 1:
            return [strs]
        
        res = dict()
        for s in strs:
            count = [0] * 26 ## for a, ... z
            for c in s:
                count[ord(c) - ord("a")] += 1 ## track the character

            if tuple(count) in res:
                res[tuple(count)].append(s)
            else:
                res[tuple(count)] = [s]
                
        return list(res.values())