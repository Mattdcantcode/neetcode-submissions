class Solution:
    def isValid(self, s: str) -> bool:
        d = []
        p = {"[":"]","{":"}","(":")"}
        n = len(s)
        for i in range(n):
            if s[i] in p.keys():
                d.append(s[i])
                print(d)
            elif d == []:
                return False
            else:
                print(d)
                a = d.pop()
                if p[a] == s[i]:
                    continue
                else: 
                    return False
        if d == []:
                return True
        else: 
            return False
        

