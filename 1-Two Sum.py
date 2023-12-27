# Time complexity: O(n^2)
# Space complexity: O(1)

# Brute Force Solution
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)): # O(n)
            for j in range(len(nums)): # O(n)
                # when the sum of different element equal to the target
                if i != j and nums[i]+nums[j] == target:
                    # return the index of both element
                    return [i,j]