## Sol 1
# Runtime: 40 ms, faster than 81.82% of Python3 online submissions for Bulls and Cows.
# Memory Usage: 14.2 MB, less than 83.57% of Python3 online submissions for Bulls and Cows.

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        ## initiate value for A and B
        result = [0, 0]
        
        ## check for bulls
        for s, g in zip(secret, guess):
            if s == g: ## check if the values are the same
                result[0] += 1
        
        ## check for cows
        ## use hashmap to loop through all numbers
        dic = {}
        for s in secret:
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1
        
        for g in guess:
            if g in dic:
                if dic[g] > 0:
                    dic[g] -= 1
                    result[1] += 1
        
        ## get B's by dividing A's
        result[1] -= result[0]
        
        return str(result[0]) +'A' + str(result[1]) + 'B'
    
    
## Sol 2
# Runtime: 40 ms, faster than 81.82% of Python3 online submissions for Bulls and Cows.
# Memory Usage: 14.3 MB, less than 60.89% of Python3 online submissions for Bulls and Cows.

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        d1 = {}
        d2 = {}
        bull = 0
        cow = 0
        
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                if secret[i] in d1:
                    d1[secret[i]] += 1
                else:
                    d1[secret[i]] = 1
                
                if guess[i] in d2:
                    d2[guess[i]] += 1
                else:
                    d2[guess[i]] = 1
        
        
        for i in d1:
            if i in d2:
                cow += min(d1[i], d2[i])
        
        
        return str(bull) + 'A' + str(cow) + 'B'