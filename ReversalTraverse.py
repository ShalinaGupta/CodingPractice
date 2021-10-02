class Solution:

    def countEven(this, A):
        count = 0
        for item in A:
            if item%2==0:
                count+=1
        return count


    def evenNum(this, A):

        cnteven = this.countEven(A)
        originalIndx = len(A) - 1
        A = A + [-1]*cnteven
        #A = [2,2,4,4,0,0,1,3]
        updtdLastIndex = len(A) - 1

        while updtdLastIndex>=0:
            if A[originalIndx]%2==0:
                A[updtdLastIndex] = A[originalIndx]  
                updtdLastIndex -=1          #3
                
            A[updtdLastIndex] = A[originalIndx]
            updtdLastIndex -=1
            originalIndx -=1

        return A


A = [2,4,0,1,3]
sol = Solution()
output = sol.evenNum(A)
print(output)





