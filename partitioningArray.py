
class Solution:

    def arrpart(this, A):
        
        startIndex = 0
        
        for elemIndex in range(0,len(A)):
            if A[elemIndex] == 0:
                A[startIndex], A[elemIndex] = A[elemIndex], A[startIndex]
                startIndex+=1
        return A   




   


A = [1,2,3,0,8,9,0,6,0,6] #immutable
#A = []

sol = Solution()
output = sol.arrpart(A)
print (output)



