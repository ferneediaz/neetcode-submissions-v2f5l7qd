from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        cur_consecutive = 0
        for num in nums:
            if num == 1:
                cur_consecutive += 1
                max_consecutive = max(cur_consecutive,max_consecutive )
            else:
                cur_consecutive = 0
        return max_consecutive