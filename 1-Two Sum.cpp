#include <iostream>
#include <vector>

// Time complexity: O(n^2)
// Space complexity: O(1)      
// bruce force

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size();i++){
            for (int j = 0; j < nums.size();j++) {
                if (i != j && nums.at(i) + nums.at(j) == target) {
                    return vector<int>{i,j};
                }
            }
        }
        return vector<int>{};
    }
};

// Time complexity: O(n)
// Space complexity: O(1)   
// hash table

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (numMap.count(complement)) {
                return {numMap[complement], i};
            }
            numMap[nums[i]] = i;
        }
        return {}; // No solution found
    }
};