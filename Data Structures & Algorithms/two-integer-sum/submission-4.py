class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashM = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashM:
                return [hashM[diff], i]
            hashM[n] = i