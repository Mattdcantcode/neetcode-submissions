class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        print(n)
        digits[n-1] += 1
       
        for i in range(n-1):
            if digits[n-1-i] == 10:
                digits[n-2-i] +=1
                digits[n-1-i] = 0
                print(digits)
            else: 
                continue
        if digits[0] == 10:
            digits[0:1] = [0]
            digits.insert(0,1)
            return(digits)
        else:
            return(digits)