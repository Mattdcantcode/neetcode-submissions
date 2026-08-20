class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        for i in range(n): 
            current_sum = numbers[left] + numbers[right] 
            if current_sum > target: 
                right -= 1
            elif current_sum < target: 
                left += 1
            else: 
                return [left + 1, right + 1]