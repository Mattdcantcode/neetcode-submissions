class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        n = int(len(strs))
        for i in range(n): 
            a = "".join(sorted(strs[i]))
            d.setdefault(a,[]).append(strs[i])
        return list(d.values())    
          



           
          
            