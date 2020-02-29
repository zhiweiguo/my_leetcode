'''
顺时针打印矩阵

'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bot = len(matrix) - 1
        if bot == -1:
            return []
        left = 0
        right = len(matrix[0]) - 1
        if right == -1:
            return []

        res = []
        while True:
            # 上， 行  （从左到右）
            for j in range(left, right+1, 1):
                res.append(matrix[top][j])
            top += 1
            if top > bot: break

            # 右， 列  （从上到下）
            for i in range(top, bot+1):
                res.append(matrix[i][right])
            right -= 1
            if right < left: break

            # 下， 行  （从右到左）
            for j in range(right, left-1, -1):
                res.append(matrix[bot][j])
            bot -= 1
            if bot < top: break

            # 左， 列  （从下到上）
            for i in range(bot, top-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right: break

        return res

           