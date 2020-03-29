# 每日打卡 day7 : 1162

'''
地图分析
N*N的地图，0代表海洋，1代表陆地，找到距离陆地区域最远的海洋区域是哪个，并返回距离
距离为曼哈顿距离
'''

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # 获取行列数
        raws = len(grid)
        cols = len(grid[0])
        start= []
        # 找到陆地所在的位置
        for i in range(raws):
            for j in range(cols):
                if grid[i][j] == 1:
                    start.append((i, j, 0))
        # 判断是否全为海洋，或者是否全为陆地
        if len(start) == 0 or len(start) == (raws * cols):
            return -1
        que = collections.deque(start)
        # 定义向上下左右四个方向移动的偏移量
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        while que:
            i, j, dis = que.popleft()
            for d in range(4):
                x = i + dx[d]
                y = j + dy[d]
                if x < 0 or y < 0 or x == raws or y == cols or grid[x][y] == 1:
                    continue
                que.append((x, y, dis+1))
                grid[x][y] = 1

        return dis 