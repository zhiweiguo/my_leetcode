'''

二进制中1的个数
请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

'''

class Solution:
    def hammingWeight(self, n):
        count = 0
        i = 0
        while n:
            if n & 1:
                count += 1
            i += 1
            n = n >> 1
        return count

    def hammingWeight_2(self, n: int) -> int:
        count = 0
        while n!=0:
            n = n & (n-1)
            count += 1
        return count


if __name__ == "__main__":
    n = 11
    sol = Solution()
    res = sol.hammingWeight(n)
    print(res)

