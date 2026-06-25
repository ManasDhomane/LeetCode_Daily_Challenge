class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)

        prefix = 0
        size = 2 * n + 3
        offset = n + 1

        bit = [0] * (size + 1)

        def update(i):
            while i <= size:
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        ans = 0
        update(offset)

        for num in nums:
            if num == target:
                prefix += 1
            else:
                prefix -= 1

            idx = prefix + offset
            ans += query(idx - 1)
            update(idx)

        return ans