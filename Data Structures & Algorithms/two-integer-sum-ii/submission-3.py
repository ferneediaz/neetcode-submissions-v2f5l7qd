class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        while L < R:
            ans = numbers[L] + numbers[R]
            if ans > target:
                R -=1
            elif ans < target:
                L +=1
            else:
                return [L + 1, R + 1]
