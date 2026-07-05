class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        y = 0
        if len(s)%2 == 0:
            for i in range(int(len(s)/2)):
                y -= 1
                if s[i] == s[y]:
                    continue
                else:
                    return False
        else:
            for i in range(int((len(s)-1)/2)):
                y -= 1
                if s[i] == s[y]:
                    continue
                else:
                    return False
        return True

