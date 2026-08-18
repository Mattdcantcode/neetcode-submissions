class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        n = len(s)
        a = 0
        b = n-1
        for _ in range(int(n/2)):
            if s[a] == s[b]:
                a += 1
                b -= 1
                continue
            else: 
                return False 
        return True
        