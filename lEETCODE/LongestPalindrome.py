#find the length of longest possible palindrome in a string 
#first of all calculate frequencies of each char if they are even store then if odd take 
#only one odd and return the length 
from collections import Counter

def longestPalindrome(s: str) -> int:
    freq = Counter(s)
    length = 0
    odd_found = False
    for count in freq.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_found = True
    if odd_found:
        length += 1  
    return length

string = "abcddeeff"
print(f"Longest Possible Palindrome in {string} is:",longestPalindrome(string))