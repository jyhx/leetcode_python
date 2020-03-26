#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # r[]表示匹配成功的括号位置
        stack, r = [], [False]*len(s)
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            elif char == ')' and stack:
                r[stack.pop()], r[index] = True, True
        cur, ret = 0, 0
        for i in r:
            if i:
                cur += 1
            else:
                ret = max(cur, ret)
                cur = 0
        ret = max(cur, ret)    
        return ret    

# @lc code=end

