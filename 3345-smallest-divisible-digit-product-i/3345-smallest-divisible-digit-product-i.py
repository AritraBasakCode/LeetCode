class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def check(num: int) -> bool:
            pdt = 1
            while num > 0:
                pdt *= num % 10
                num //= 10
                if pdt == 0:
                    break
            return pdt % t == 0
        while not check(n):
            n += 1
        return n