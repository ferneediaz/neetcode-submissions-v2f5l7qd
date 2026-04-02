class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[i] = nums[-1]  # move last element into i
                nums.pop()          # remove last element
            else:
                i += 1
        return len(nums)