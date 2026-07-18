class Solution:
    def arrayRankTransform(self, arr):
        rank = {num: i + 1 for i, num in enumerate(sorted(set(arr)))}
        return [rank[x] for x in arr]