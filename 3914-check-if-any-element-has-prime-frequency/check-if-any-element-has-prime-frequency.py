from collections import Counter

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        for count in freq.values():
            if self.isPrime(count):
                return True
        return False

    def isPrime(self, n):
        if n < 2:
            return False

        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1

        return True