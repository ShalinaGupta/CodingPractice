
class Solution:


    def sumNum(this, A, B):
        arrDict = {}

        for elem in A:
            arrDict[elem] = 1


        for elemIndex in range(len(A)):
            secElem = B-A[elemIndex]
            if arrDict.get(secElem) and secElem != A[elemIndex]:
                return A[elemIndex], secElem
        return -1



   

A = [1,2,3,4,5,6,7,8,9] #immutable
B = 12
sol = Solution()
output = sol.sumNum(A, B)
print (output)



