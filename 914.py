# 每日打卡 day5 : 914

'''
卡牌分组

给定一副牌，每张牌上都写着一个整数。
此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

示例 1：

输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
示例 2：

输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。

'''

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        '''
        对于每一个枚举到的 X，我们只要先判断 X 是否为 N 的约数，
        然后遍历所有牌中存在的数字 i，看它们对应牌的数量 count_i是否满足上述要求。
        如果都满足等式，则 X 为符合条件的解，否则需要继续令 X 增大，枚举下一个数字。

        '''
        length = len(deck)
        if length == 1:
            return False
        num_dict = {}
        for num in deck:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        vals = list(num_dict.values())
        for X in range(2, length+1):
            if length % X == 0:
                for i in vals:
                    if all(i % X == 0 for i in vals):                                      
                        return True

        return False 