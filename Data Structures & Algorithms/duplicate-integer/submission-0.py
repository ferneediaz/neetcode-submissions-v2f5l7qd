from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)  # Sort the list
        for i in range(len(nums) - 1):  # Iterate through indices
            if nums[i] == nums[i + 1]:  # Check if the current element is the same as the next element
                return True
        return False  # Return False if no duplicates are found
