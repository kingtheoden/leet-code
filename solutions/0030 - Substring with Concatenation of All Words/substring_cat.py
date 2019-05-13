import copy

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        dic = {}
        if not s or not words or not words[0]:
            return []
        length = len(words[0])
        words_length = length * len(words)

        for word in words:
            dic[word] = 1 if word not in dic.keys() else dic[word] + 1

        def helper(rest_string, dic):
            word = rest_string[0:length]
            next_word_index = length
            while word in dic.keys():
                dic[word] -= 1
                if dic[word] == 0:
                    del dic[word]
                word = rest_string[next_word_index:next_word_index + length]
                next_word_index += length
            return not dic

        for i in range(len(s)):
            if i + words_length > len(s):
                break
            if s[i:i+length] in dic.keys():
                new_dic = copy.deepcopy(dic)
                if helper(s[i:], new_dic):
                    result.append(i)

        return result
