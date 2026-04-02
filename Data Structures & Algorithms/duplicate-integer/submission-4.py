class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in nums:
            if i in hash:
                return True
            hash[i] = 99123123123123123123
        return False