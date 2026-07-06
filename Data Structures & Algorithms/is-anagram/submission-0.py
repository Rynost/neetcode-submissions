class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #checks if strings are the same length
            return False #not same length? return false
        
        countS, countT = {}, {} #create hashmaps
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #counts # of letters
            countT[t[i]] = 1 + countT.get(t[i], 0) #counts # of letters
        for c in countS:
            if countS[c] != countT.get(c, 0): #checks if don't counts match
                return False
        return True # counts match, return true