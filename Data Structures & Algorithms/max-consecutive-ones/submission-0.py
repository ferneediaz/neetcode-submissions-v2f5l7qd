from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        cur = 0
        for num in nums:
            if num == 1:
                cur += 1
                max_len = max(max_len, cur)
            else:
                cur = 0
        return max_len