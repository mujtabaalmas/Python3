
# class Solution:
#     def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
#         result = list
#         previous_group = None
#         for i in range(len(words -1)):
#             if previous_group is None or groups[i] != previous_group:
#                 result = words[i]
#                 previous_group = groups[i]
#         return result

# getSubsequence = Solution().getLongestSubsequence(["a","b","c","d","e"],[1,0,1,1,0],)
# print(getSubsequence)