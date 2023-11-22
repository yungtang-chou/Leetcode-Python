class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        hashmap = {}
        for voc in s:
            if voc in hashmap:
                hashmap[voc] += 1
            else:
                hashmap[voc] = 1
        
        for voc in t:
            if voc in hashmap and hashmap[voc] > 0:
                hashmap[voc] -= 1
            else:
                return False
        if sum(hashmap.values()) > 0:
            return False
        return True
