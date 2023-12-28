// Time complexity: O(n^2)
// Space complexity: O(1)      
// bruce force

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    for (int i = 0; i < numsSize ; i++) {
        for (int j = 0; j < numsSize ; j++) {
            // loop the num and find the num that fulfil the requirements
            if (i != j && nums[i] + nums[j] == target) {
                *returnSize = 2;
                int* ans = (int*)malloc(*returnSize * sizeof(int));
                ans[0] = i;
                ans[1] = j;
                return ans;
            }
        }
    }
    *returnSize = 0; // return size 0 if no valid pair found
    return NULL;
}