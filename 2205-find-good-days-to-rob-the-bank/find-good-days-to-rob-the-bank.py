class Solution:
    def goodDaysToRobBank(self, security, time):
        n = len(security)

        if time == 0:
            return list(range(n))

        left = [0] * n
        right = [0] * n

        # Count non-increasing days ending at i
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1

        # Count non-decreasing days starting at i
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1

        ans = []
        for i in range(time, n - time):
            if left[i] >= time and right[i] >= time:
                ans.append(i)

        return ans