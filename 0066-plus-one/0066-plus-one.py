class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for digit in digits:
            number = number * 10 + digit
        number += 1

        new_digits = []
        while number>0:
            l_digit = number%10
            new_digits.append(l_digit)
            number = number //10

        new_digits.reverse()

        return new_digits