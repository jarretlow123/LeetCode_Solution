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
                
# Time complexity: O(n)
# Space complexity: O(1)      
# Hash Table

class Solution(object):
    def twoSum(self, nums, target):
        val = {}

        for i in range(len(nums)):
            # find the complement
            x = target - nums[i]
            # if complement is in the table return the result
            if x in val.keys():
                return [val[x],i]
            # add the value and it's index to table
            val[nums[i]]= i
