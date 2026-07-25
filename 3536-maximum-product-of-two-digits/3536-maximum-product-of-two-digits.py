class Solution:
    def maxProduct(self, n: int) -> int:
        largest = 0
        secondLargest = 0

        while n > 0:
            digit = n % 10

            if digit > largest:
                secondLargest = largest
                largest = digit
            elif digit > secondLargest:
                secondLargest = digit

            n //= 10

        return largest * secondLargest
        