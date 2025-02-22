#TC-O(n^2), SC -O(1), since I'm returning dp1, it's not auxillary space
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp1=[]
        for i in range(numRows):
            dp2=[None for _ in range(i + 1)]
            dp2[0]=dp2[-1]=1
            for j in range(1, len(dp2) - 1):
                dp2[j]=dp1[i - 1][j - 1]+dp1[i - 1][j]
            dp1.append(dp2)
        return dp1