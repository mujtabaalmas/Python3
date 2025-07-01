## infinite generator printing palindromes-------------------
# def infinite_sequence():
#     n=0
#     while True:
#         yield n 
#         n+=1

## Example of infinite_sequence generator
## x = infinite_sequence()
## x= next(infinite_sequence())
## print(x)

# def is_palindrome(num):
#     if num // 10 == 0:
#         return False
#     temp = num
#     reversed_num = 0

#     while temp != 0:
#         reversed_num = (reversed_num * 10) + (temp % 10)
#         temp = temp // 10

#     if num == reversed_num:
#         return num
#     else:
#         return False
    
# for i in infinite_sequence():
#     pal = is_palindrome(i)
#     if pal:
#         print(i)

##--------------------------------------------------------------##
1223221
##generator send throw and close operations --------------------
def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False
    
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1

# pal_gen = infinite_palindromes()
# for i in pal_gen:
#     digits = len(str(i))
#     pal_gen.send(10 ** (digits))

pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        #pal_gen.throw(ValueError("We don't like large palindromes"))
        pal_gen.close()
    print(10 ** (digits))
    pal_gen.send(10 ** (digits))

    ##------------------------------------------------------------------##

