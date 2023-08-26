#Find Anagram

#Sort Method

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True
        else:
            return False


#Hashmap Method

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        HashS, HashT = {}, {}

        for i in range(len(s)):
            HashS[s[i]] = 1 + HashS.get(s[i], 0)
            HashT[t[i]] = 1 + HashT.get(t[i], 0)

        # You can compare the Hashmap directly
        if HashS == HashT:
            return True
        else:
            return False

        # Or Iterate over the Dict to compare values
        for keys in HashS:
            if HashS[keys] != HashT.get(keys, 0):
                return False

        return True
