class Solution:
    def sumOfDigits(self, n):
        sum = 0
        while n > 0:
            sum += n % 10
            n //= 10
        
        return sum