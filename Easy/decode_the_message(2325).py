import string


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        letters_hashmap = {}
        letters_generator = (letter for letter in string.ascii_lowercase)
        for letter in key.replace(" ", ""):
            if letter in letters_hashmap.keys():
                continue
            letters_hashmap[letter] = next(letters_generator)
        result = [letters_hashmap.get(letter, " ") for letter in [
            word for word in message
        ]]
        return ''.join(result)


solution = Solution()
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(solution.decodeMessage(key, message))
