class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashhash = set()
        for num in nums:
            if num in hashhash:
                return True
            hashhash.add(num)
        return False