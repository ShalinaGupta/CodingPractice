class Solution:

    

    def revArr(this, A):

        lenA = len(A)
        

        for elemIndex in range(lenA//2):
            A[elemIndex], A[lenA-1-elemIndex] = A[lenA-1-elemIndex], A[elemIndex]
        return A

      

A = [9,8,7,6,5,4,3,2,1] #immutable
sol = Solution()
output = sol.revArr(A)
print (output)
