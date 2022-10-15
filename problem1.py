import math


class Solution:
    def countall(self, n_customers: int) -> int:

        num = (math.trunc(math.log(n_customers, 10)) + 1) * 9 + 1
        res = [0] * num
        for i in range(n_customers):
            a = i
            x = 0
            while a > 0:
                x += (a % 10)
                a = a // 10
            res[x] += 1
        i = num - 1
        while (i >= 0) and (res[i] == 0):
            res.pop(i)
            i -= 1
        return res


sol = Solution()
print(sol.countall(100))
