'''
有效括号的嵌套深度
'''

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        '''
        没看懂题意
        '''
        
        ans = []
        d = 0
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d % 2)
            if c == ')':
                ans.append(d % 2)
                d -= 1
        
        return ans