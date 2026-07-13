class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        averages = set()

        left = 0
        right = len(nums) - 1

        while left < right:
            averages.add((nums[left] + nums[right]) / 2)
            left += 1
            right -= 1

        return len(averages)