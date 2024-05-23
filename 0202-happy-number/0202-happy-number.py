class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        
        while n not in check:
            check.add(n)
            
            n = self.square_helper(n)
            
            if n == 1:
                return True
            
        return False
        
       
    def square_helper(self, n: int) -> int:
        output = 0

        while n>0:

            last_digit = n%10
            
            last_digit = last_digit**2

            output += last_digit

            n = n//10

        return output

        
        
        
        