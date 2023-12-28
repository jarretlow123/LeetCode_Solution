# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs = sorted(strs)
        s = ""
        # loop the shortest string
        for i in range(min(len(strs[0]),len(strs[-1]))):
            # compare the first element and last element
            # since the list is sorted the common prefix can compare within the first and last element
            if strs[0][i] == strs[-1][i]:
                # if same add the char
                s += strs[0][i]
            # not same then return the result
            else:
                return s
            
        # if the list contain only empty string return back the empty string
        return strs[0]
    
