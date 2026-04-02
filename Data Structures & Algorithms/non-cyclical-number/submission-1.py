"""
Assumptions/Constraints 
Int is positive
replace it with the sum of the squares of its digits
repeat until number equals one, 
loops infinitly 

Approach Ideas:
if we see the same number twice we know its an infinite loop 





"""





class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        

        while n!= 1:
            summ = 0
            if n in seen:
                return False
            seen.add(n)
            digits = [int(d) for d in str(n)]
            for d in digits:
                summ += d **2
            n = summ

        return True
        