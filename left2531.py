class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        word1 = set(word1)
        word2 = set(word2)
        if len(word1) == len(word2):
            return True

        if len(word2) < len(word1):
            word2, word1 = word1, word2

        if (len(word2) - len(word1)) == 1:
            if len(word2 - word1) > 0 and len(word1 - word2) > 0:
                return True

        return False
