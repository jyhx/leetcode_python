#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        word_dict = {}
        word_len = len(words[0])
        word_nr = len(words)
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict.update({word: 1})
        ret = []
        for i in range(len(s)-word_nr*word_len+1):
            flag = True
            substring_dict = {}
            for k in range(word_nr):
                word_window = s[i+k*word_len:i+(k+1)*word_len]
                if word_window not in word_dict:
                    flag = False
                    break
                if word_window in substring_dict:
                    if substring_dict[word_window] < word_dict[word_window]:
                        substring_dict[word_window] += 1
                    else:
                        flag = False
                        break
                else:
                    substring_dict.update({word_window:1})
            if flag:
                ret.append(i)
        return ret
# @lc code=end
