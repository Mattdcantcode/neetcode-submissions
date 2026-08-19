class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        d = []
        while l < r: 
            dif = r - l 
            if heights[r] > heights[l]:
                d.append(heights[l]*dif)
                l += 1
            else:
                d.append(heights[r]*dif)
                r -= 1
        return max(d)
             


            