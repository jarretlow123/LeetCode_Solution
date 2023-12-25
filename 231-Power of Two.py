import math

class Solution:
    def isPowerOfTwo(n: int) -> bool:
        # y = b^x -> x = logb y
        if n <=0:
            return False
        return math.log2(n) % 1 == 0 

class Solution2:
    def isPowerOfTwo(n: int) -> bool:
        # print(bin(n),bin(n)[2])
        # result of bin(n) is 0bXXXXXX 0B indicate that this is binary and XXX is binary code  
        return bin(n)[2] == "1" and bin(n).count("1") == 1
    
if __name__ == "__main__":
    print(Solution.isPowerOfTwo(1))
    print(Solution2.isPowerOfTwo(1))