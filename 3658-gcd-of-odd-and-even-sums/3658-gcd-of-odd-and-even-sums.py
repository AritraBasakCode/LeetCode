class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        #gcd(n^2, n(n+1)) = n × gcd(n,n+1)
        #gcd(n,n+1)=1
        #gcd(n^2, n(n+1))=n
        return n