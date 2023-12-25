# solution 1
class Solution:
    def sortBremainderBits(self, arr):

        result = []

        # get and list the number of 1 bit
        val = [[bin(i).count('1') for i in arr],[i for i in arr]] 

        # arrange the list
        for i in list(set(val[0])):
            temp = []
            for j in range(len(val[0])):
                if val[0][j] == i:
                    temp.append(val[1][j])
            temp.sort()
            for j in temp:
                result.append(j)

        return result

# solution 2
class Solution2:
    def sortBremainderBits(self, arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
    
if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(Solution.sortBremainderBits(0, arr))
    print(Solution2.sortBremainderBits(0, arr))
