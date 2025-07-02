#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
            stack = []
            mapping = {')': '(', '}': '{', ']': '['}
            for i in s:
                if i in mapping.values():
                    stack.append(i)
                elif i in mapping:
                    if not stack or stack[-1] != mapping[i]:
                        return False
                    stack.pop()
                else:
                    return False
            return not stack 

x = Solution()
somestring = "({[]})"
print(f"Valid Parathesis in str {somestring} is :",x.isValid(somestring))

# ---------------------above below practice only ----------------------

# #stack = ["([])"]
# def ok(stack):
#     if len(stack) % 2 == 0:
#         return True
#     else:
#         return False
  
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for i in s:
#             stack.append(s)
#             if stack.pop == stack.append(s):
#                 return i
#         if stack.
#         return i
            

# x = Solution()
# s= "()"

# print(x.isValid(s))

# stack = "({[]})"

  
# if ok(stack):
#     print("Stack is Even")
#     print(stack)
# else:
#     print("Stack is Odd")
#     print(stack)
#--------------------------
#str = "({[]})","()","(}","(){}[]"

        #         if stack.append[i] == s(i):
        #             if stack.pop[i] == s(i+1):
        #                 stack.pop[i]
        #     #             i+=1
        #     return True
        # else:
        #     return False
        


    
