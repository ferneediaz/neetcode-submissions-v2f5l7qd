class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []  # Store all valid combinations

        def dfs(i, cur, total):
            """
            Depth-first search to explore combinations.
            
            i     : current index in nums (decides which number we're allowed to take)
            cur   : current combination list being built
            total : sum of numbers in cur
            
            Decision tree branches:
            1. TAKE nums[i] → stay at same index i (unlimited use)
            2. SKIP nums[i] → move to index i+1
            """
            
            # Base case: found a valid combination
            if total == target:
                res.append(cur.copy())  # Append a copy, since cur will be modified later
                return
            
            # Prune invalid paths: exceeded target or ran out of numbers
            if i >= len(nums) or total > target:
                return

            # --- Decision 1: TAKE nums[i] (stay at i for unlimited repeats) ---
            cur.append(nums[i])          # Add current number to combination
            dfs(i, cur, total + nums[i]) # Recurse: stay at i, total increases
            # Example: nums=[2,5,6,9], target=9
            #   take 2 → cur=[2], total=2 → recurse at i=0
            #     take 2 → cur=[2,2], total=4 → recurse at i=0
            #       take 2 → cur=[2,2,2], total=6 → ...
            #         take 2 → cur=[2,2,2,2], total=8 → ...
            #           take 2 → cur=[2,2,2,2,2], total=10 > target → return
            #         back to total=8, skip 2 → i+1 → try 5, etc.
            
            cur.pop()                    # Backtrack: remove the number we just added
            
            # --- Decision 2: SKIP nums[i] (move to next index) ---
            dfs(i + 1, cur, total)       # Recurse without current number
            # Example: from cur=[2,2], total=4, skip 2 → try 5,6,9
            #   take 5 → cur=[2,2,5], total=9 == target! Add to res

        # Start recursion from index 0, empty combination, total 0
        dfs(0, [], 0)
        return res