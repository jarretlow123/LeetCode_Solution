# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = ['I','V','X','L','C','D','M']
        val = [1,5,10,50,100,500,1000]

        ans = 0
        # loop the given string 
        for i in range(len(s)-1):
            # check the roman number to decide is minus or plus by compare the index of the roman number
            if roman.index(s[i]) >= roman.index(s[i+1]):
                ans += val[roman.index(s[i])]
            else:
                ans -= val[roman.index(s[i])]

        return ans + val[roman.index(s[-1:])]

# Time complexity: O(n)
# Space complexity: O(1)
# using hash table

class Solution2:
    def romanToInt(self, s: str) -> int:
        # prepare the hash table
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        # loop the given string
        for i in range(len(s)):
            # check is lask char or not
            # check the value of the roman number to decide is plus or minus
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans