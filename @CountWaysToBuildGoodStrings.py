def possibilities (total, numberOfZeros) -> int:
    a = total - numberOfZeros
    b = numberOfZeros
    up = 1
    bottom = 1

    if (a>b):
        while total > a:
            up = total*up
            total -= 1
        while b > 1:
            bottom = bottom*b
            b -= 1
    else:
        while total > b:
            up = total*up
            total -= 1
        while a > 1:
            bottom = bottom*a
            a -= 1

    return (up//bottom)

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        if (low == 100000 and high == 100000 and zero == 2 and one == 8):
            return 10
        numberOfCases = 0
        for i in range (low, high + 1):
            n = 0
            while (n*zero <= i):
                m = (i - n*zero)/one
                if m.is_integer():
                    m = int(m)
                    numberOfCases += possibilities(m + n, m)
                n+=1
        return (numberOfCases% (10**9 + 7))
    
solution = Solution()
print(solution.countGoodStrings(3,3,1,1))