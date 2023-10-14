class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == len(word2):
            return ''.join([''.join(item) for item in zip(word1, word2)])
        else:
            min_length = min([len(word1), len(word2)])
            result_list = [''.join(item) for item in zip(word1, word2)]
            if len(word1) > min_length:
                for letter in list(word1)[min_length:]:
                    result_list.append(letter)
            elif len(word2) > min_length:
                for letter in list(word2)[min_length:]:
                    result_list.append(letter)
            return ''.join(result_list)