
class Solution:

    def arrpart(this, A):
        
        endIndex = len(A)-1
        countZero = 0

        currIndex = len(A) -1

        while(currIndex>=0):
            if A[currIndex] ==0:
                countZero+=1
                currIndex -=1
                continue
            A[endIndex] = A[currIndex]
            endIndex -= 1
            currIndex -= 1

        A[:countZero] = [0]*countZero
        return A

            

        
        for currIndex in range(len(A)-1, -1, -1):
            if A[elemIndex] == 0:
                A[startIndex], A[elemIndex] = A[elemIndex], A[startIndex]
                startIndex+=1
        return A   




A = [1,2,3,0,8,9,0,6,0,6] #immutable
#A = []

sol = Solution()
output = sol.arrpart(A)
print (output)



