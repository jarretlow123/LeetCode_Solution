# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert to string, and reverse it and check it
        return str(x) == str(x)[::-1]
    
# Time complexity: O(n)
# Space complexity: O(1)

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        # if the value is negative, due to the present of sign (-) so it confirm not a palindrome number
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        # reserve the integer 
        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return reversed_num == x