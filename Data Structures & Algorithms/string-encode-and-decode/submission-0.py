class Solution:

    def encode(self, strs: List[str]) -> str:
       
        encode = ""
        for i in range(len(strs)):
            n = str(len(strs[i]))
            add = "#".join([n,strs[i]])
            encode = "".join([encode,add])
        return encode

    def decode(self, s: str) -> List[str]:
        counter = 0
        decoded = []
        while counter < len(s):
            j = s.find("#",counter)
            length = int(s[counter:j])
            decoded.append(s[j+1:j+1+length])
            counter = j + 1 + length
        return decoded
             
            
