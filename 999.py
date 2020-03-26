# 每日打卡 day4 : 999

'''
车的可用捕获量

'''

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        '''
        先找到白色车'R'的位置对应的索引
        再从该位置分别往4个方向搜索，
        碰到'B',则该方向搜索结束；
        碰到'p',则计数+1，该方向搜索结束；
        索引超出有效边界，该方向搜索结束
        '''
        # 往上，下，左，右移动对应的x,y坐标的偏移
        tx = [-1, 1, 0, 0]
        ty = [0, 0, -1, 1]
        x = 0
        y = 0
        count = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x = i
                    y = j
                    break
        for i in range(4):
            for j in range(8):
                xx = x + j*tx[i]
                yy = y + j*ty[i]
                if xx < 0 or xx >= 8 or yy < 0 or yy >= 8 or board[xx][yy] == 'B':
                    break
                if board[xx][yy] == 'p':
                    count += 1
                    break
        
        return count
