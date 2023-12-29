// Time complexity: O(n)
// Space complexity: O(1)
// brute force

var twoSum = function(nums, target) {
    const map = new Map();

    for (var i = 0; i < nums.length; i++) {

        var complement = target - nums[i]

        if (map.has(complement)) {
            return [i,map.get(complement)]
        }

        map.set(nums[i],i)
    }
};

// Time complexity: O(n^2)
// Space complexity: O(1)
// hash table

var twoSum = function(nums, target) {
    let map=new Map();
    for (var i = 0; i < nums.length; i++) {
        if (map.has(target - nums[i])) {
            return [i,map.get(target - nums[i])]
        }
        map.set(nums[i],i)
    }
};