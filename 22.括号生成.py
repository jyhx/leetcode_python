#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def dfs(n, s, nr_l, nr_r,):
            if nr_r > nr_l or nr_l > n or nr_r > n:
                return
            if nr_l == n and nr_r == n:
                ret.append(s)
                return
            dfs(n, s+'(', nr_l+1, nr_r)
            dfs(n, s+')', nr_l, nr_r+1)
            return
        dfs(n, '', 0, 0)
        return ret

# @lc code=end
