class Solution:
    def __init__(self):
        pass
    def hashstring(self, s: str) -> str:
        chars = [0]*26
        for i in s:
            chars[ord(i)-ord('a')] +=1
        res=''
        for i in range(26):
            if chars[i]!=0:
                res = res+f"{chr(i+ord('a'))}"+f"{chars[i]}"
        return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        result=[]
        for i in strs:
            hashstr = self.hashstring(i)
            if hashstr in d:
                d[hashstr].append(i)
            else:
                d[hashstr]=[i]
        for i in d:
            result.append(d[i])
        return result