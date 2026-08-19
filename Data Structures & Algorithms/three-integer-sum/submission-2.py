class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        n = len(s)
        d = []
        for i in range(n):
            if i > 0 and s[i] == s[i-1]:
                continue
            l = i + 1 
            r = n - 1
            while l < r: 
                total = s[i] + s[l]+ s[r]
                if total > 0: 
                    r -= 1
                elif total < 0: 
                    l += 1
                elif total == 0: 
                    ans = [s[i],s[l],s[r]]
                    d.append(ans)
                    
                    while l < r and s[l] == s[l+1]:
                        l += 1
                    while r > l and s[r] == s[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                    continue
            
                    
            
        
        return d
