import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.lower()
        for i in range(len(s)):
            print(s[i],s[len(s)-i-1])
            if s[i]!=s[len(s)-i-1]:
                return False
        else:
            return True