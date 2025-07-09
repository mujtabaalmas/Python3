#Given an integer n, return an array ans of length n + 1 such that for each i 
#(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1) 
    return ans

print("No. of Bits: ",countBits(5))  
#print("No. of Bits: ",countBits(7))  
#------------------------------------------------------#
    
#Given a positive integer n, write a function that returns the number of set bits in 
#its binary representation (also known as the Hamming weight).

def hammingWeight(n: int) -> int:
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count

print("Hamming Weight of 5: ",hammingWeight(5))
#print("Hamming Weight of 7: ",hammingWeight(7))
#-------------------------------------------------------------#

#it can also be done using built-in function 
def hammingWeight2(n):
    return bin(n).count('1')

print("Hamming Weight of 7: ",hammingWeight2(7))

#-------------------------------------------------------------#