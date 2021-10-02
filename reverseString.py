class Solution:

    def revSent(this, A):

        newStr = ""
        wordEnd = len(A)

        for elemIndex in range(len(A)-1, -1, -1):
            if A[elemIndex] == ' ':
                newStr+= A[elemIndex+1:wordEnd]
                newStr += A[elemIndex]
                wordEnd = elemIndex

        newStr += A[:wordEnd]

        return newStr

A = " I love NY and cal" #immutable
sol = Solution()
output = sol.revSent(A)
print (output)
