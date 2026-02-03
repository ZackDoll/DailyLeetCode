class Solution:
    def fib(self, n: int) -> int:
        f1 = 1
        f2 = 1
        if n == 0:
            return 0
        if n == 1 or n==2:
            return 1
        
        for _ in range(n-2):
            temp = f2
            f2 += f1
            f1 = temp
            
        return f2
