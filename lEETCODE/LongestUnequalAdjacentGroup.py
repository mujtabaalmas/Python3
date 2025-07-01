#You are given a string array words and a binary array groups both of length n.
# A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements at the same indices in groups are different (that is, there cannot be consecutive 0 or 1).
# Your task is to select the longest alternating subsequence from words.
# Return the selected subsequence. If there are multiple answers, return any of them.
# Note: The elements in words are distinct.

class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        result = []
        prevoius_group = None

        for i,j in zip(words,groups):
                if prevoius_group is None or j != prevoius_group:
                    result.append(i)
                    prevoius_group = j
        return result
            
ret = Solution().getLongestSubsequence(["a","b","c","d","e","f"],[1,0,1,1,1,0])
print(ret)
ok = Solution().getLongestSubsequence(["a","b","c","d","e","f","g","h","i","j","k","l"],[1,0,1,1,1,0,1,0,1,1,1,0])
print(ok)