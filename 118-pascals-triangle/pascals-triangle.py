class Solution:
    def generate(self, n: int):
        ans = []
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = ans[i - 1][j - 1] + ans[i - 1][j]
            ans.append(row)
        return ans