// Time complexity: O(n)
// Space complexity: O(n)
// hash table

import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // prepare a hash table to store the value
        Map<Integer, Integer> complementMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            // find complement
            int complement = target - nums[i];
            
            if (complementMap.containsKey(complement)) {
                // if complement exists in the map, return the indices of the two numbers
                return new int[]{complementMap.get(complement), i};
            }
            
            // append the value and index to hash table
            complementMap.put(nums[i], i);
        }
        
        // If no solution is found, return an empty array
        return new int[0];
    }
}

// Time complexity: O(n^2)
// Space complexity: O(1)
// brute force

class Solution2 {
    public int[] twoSum(int[] nums, int target) {
        for (int i =0; i < nums.length;i ++ ) {
            for (int j = 0; j < nums.length;j++) {
                // find the two number that fulfil the requirement
                if (i != j && (nums[i] + nums[j] == target)) {
                    return new int[]{i,j};
                }
            }
        }
        return new int[0];
    }
}