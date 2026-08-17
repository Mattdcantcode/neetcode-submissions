class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        a = []
        for i in range(n):
            a.append(s[-1-i]) 
        if a == list(s) or n == 1:
            return True
        else: 
            return False
