class Solution:

    def swap(self, A, B):
        return B, A
        
    def solve(self, A):
        lenA = len(A)

        for elemIndex in range(lenA//2):
            A[elemIndex], A[lenA-elemIndex-1] = self.swap(A[elemIndex], A[lenA-elemIndex-1])
        return A

sol = Solution()
A = [2, 4, 6, 2, 1]
output = sol.solve(A)
print(output)
