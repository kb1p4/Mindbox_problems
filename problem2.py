class Solution:
    def countrange(self, n_customers: int, n_first_id: int) -> int:

        resID = []
        resSUM = []
        res = []

        for i in range(n_first_id, n_first_id + n_customers):
            a = i
            x = 0

            while a > 0:
                x += (a % 10)
                a = a // 10
            resID.append(x)
            i = resID.index(x)
            if i == len(resID) - 1:
                resSUM.append(1)
            else:
                resID.pop(len(resID) - 1)
                resSUM[i] += 1

        for i in range(len(resID)):
            res.append([resID[i], resSUM[i]])
        res.sort()

        return res


sol = Solution()
print(sol.countrange(1000, 100))
