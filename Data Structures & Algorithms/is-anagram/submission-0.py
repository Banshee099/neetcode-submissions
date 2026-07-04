class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d= {}
        for i in s:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        d1 = {}
        for j in t:
            if j in d1:
                d1[j]=d1[j]+1
            else:
                d1[j]=1
        if d1 == d:
            return True
        return False