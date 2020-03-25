# 每日打卡 day3 : 892

'''
三椎形体的表面积

在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
请你返回最终形体的表面积。

'''

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        '''
        官方题解：较难理解
        若v>0，则顶面和底面分别贡献一个面，共计2个表面积
        对于4个侧面，依次判断与之相邻的位置的值，
        只有当v大于相邻位置的值nv时，才可以贡献表面积n-nv
        否则不贡献表面积

        ps: 其实该方法也可以按照下面的更简洁的方法优化，只判断同行左列，上一行同列即可
        
        '''
        n = len(grid)
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    ans += 2
                    # 依次判断该点上下左右4个点处的值
                    for r, c in ((i-1,j), (i, j-1), (i+1, j), (i, j+1)):
                        if (r >= 0 and r < n) and (c >= 0 and c < n):
                            val = grid[r][c]
                        else:
                            val = 0
                        ans += max(grid[i][j]-val, 0)
        
        return ans

    def surfaceArea_2(self, grid: List[List[int]]) -> int:
        '''
        更简洁的方法：
        统计立方体个数block，则共有block*6个面
        统计每个位置由于上下堆叠而覆盖住几个面，即val-1
        统计每个位置的左面位置和上面位置的值，分别于当前位置的值比较，最小值就是侧面盖住的面数
        '''
        n = len(grid)
        block = 0
        cover = 0
        for i in range(n):
            for j in range(n):           
                val = grid[i][j]
                # 统计block数
                block += val
                # 统计由于上下堆叠而盖住的面（仅当val>0时有效）
                cover += val-1 if val else 0
                # 当上一行有效时，统计上一行同列的位置与当前位置的最小值
                if i > 0:
                    cover += min(grid[i-1][j], val)
                # 当左边列有效时，统计同一行左边列的位置与当前位置的最小值
                if j > 0:
                    cover += min(grid[i][j-1], val)
        
        # 无覆盖的总面数 - 盖住的面数*2
        return block*6 - cover*2

