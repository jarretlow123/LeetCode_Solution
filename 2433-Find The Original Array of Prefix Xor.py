class Solution2: 
    def findArray(self, pref):

        res = [pref[0]]

        for i in range(len(pref)-1):
            print(i)
            res.append(pref[i] ^ pref[i+1])

        return res
            
class Solution: 
    def findArray(self, pref):
        return [pref[0]] + [pref[i] ^ pref[i-1] for i in range(1, len(pref))]
            
arr = [5,2,0,3,1]
print(Solution2.findArray(0,arr))