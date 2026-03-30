class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        characterCounts = {}
        for i in range(len(s)):
            if(s[i] in characterCounts):
                characterCounts[s[i]] += 1
            else:
                characterCounts[s[i]] = 1
            if(t[i] in characterCounts):
                characterCounts[t[i]] -= 1
            else:
                characterCounts[t[i]] = -1
        for val in characterCounts.values():
            if(val != 0):
                return False
        return True