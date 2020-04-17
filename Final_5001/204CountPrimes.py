'''
(Leetcode ​ ​204 ) Count Primes
统计所有小于非负整数 n 的质数的数量。

示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''

# Third try: runtime 30%
class Solution:
    # Store the multiples of the prime number as False
    # but let j begin from i*i, as factors smaller than i have been calculated
    # for example, when i=5, 2*5 and 3*5 had been calculated when i=2 and i=3
    def countPrimes(self, n: int) -> int:
        # base case: when n=0 or n=1, no prime
        if n < 2:
            return 0
        # initialize the prime list to be n times True
        # use the list to record the numbers of prime
        prime = [True] * n
        # initialize 0 and 1 to be False
        prime[0] = prime[1] = False
        # sqrt the n to improve the efficiency
        mid = int(n**0.5)+1
        for i in range(2, mid):
            # begin j from i*i,
            # add i each for loop representing the multiple of i,
            # make prime[j]=False reducing the number of prime
            for j in range(i * i, n, i):
                prime[j] = False
        # return the total number of True-the number of prime
        return sum(prime)

# # First try: Time Limit Exceeded
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         count = 0
#         def isPrime(m):
#             if m == 1:
#                 return False
#             if m == 2 or m == 3:
#                 return True
#             for i in range(2, int(m**0.5)+1):
#                 if m % i == 0:
#                     return False
#             return True
#         for m in range(1, n):
#             if isPrime(m):
#                 count += 1
#         return count

# # Second try: runtime 13%
# # Store the multiples of the prime number as False
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n < 2:
#             return 0
#         prime = [True] * n
#         prime[0] = prime[1] = False
#         mid = int(n**0.5)+1
#         for i in range(2, mid):
#             for j in range(2, n//i + 1):
#                 if i * j < n:
#                     prime[i * j] = False
#         return sum(prime)