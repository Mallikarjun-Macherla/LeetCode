class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        Sum = 0
        product = 1

        while temp > 0:
            digit = temp % 10
            Sum += digit
            product *= digit            
            temp //= 10
        return product - Sum
