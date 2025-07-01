# to find greater number -----------
a = lambda x,y: x if x > y else y 
print(a(10, 20), "is greater ")  

#to sort a list of tuples by second element -----------
pairs = [(4,8),(1, 2), (7, 4), (9, 3), (2, 4)]
sorted_pairs =  sorted(pairs, key = lambda sorted_pairs: sorted_pairs[1])
print("Sorted by key value Y: ",[sorted_pairs])

#to find even numbers in a list -----------
list_of_numbers = [1,2,4,6,7,3,5,8,0,12,14,16,18,20]
evennum=  list(filter(lambda x: x % 2== 0 ,list_of_numbers))
print("Even numbers: ", evennum)

#to sort dictionary by key age ----------
people = [{'name': 'Ali', 'age': 25}, {'name': 'Sara', 'age': 19}, {'name': 'John', 'age': 30},{'name': 'Zara', 'age': 22}]

x= input("Enter age to sort by age only: ").strip()

sorted_people = sorted(people, key=lambda person: person[x])
print("SORTED PEOPLE BY AGE: ",sorted_people)

#find length of string in a list of strings ----------
list_of_strings = ['apple', 'banana', 'cherry', 'date']
lengths = list(map(lambda x: len(x), list_of_strings))
print(f"Lengths of strings in the list: {list_of_strings}", lengths)
# another method to print length of  the string 
# for i in range(len(list_of_strings)):
#     print(f"Length of '{list_of_strings[i]}' is {lengths[i]}")


# lambda to multiply 3 numbers ----------
multily = lambda aa,bb,cc: aa * bb * cc
print("Multiplication of 3 numbers: ", multily(7,3, 4))

# Conditionals Statements with Lambda -----
x =10 
y=20 
z=30
lambda_condition = lambda x, y, z: "x is greater" if x > y and x > z else "y is greater" if y > z else "z is greater"
print(lambda_condition(x, y, z))

# Lambda with filter to find odd numbers in a list -----
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 !=0, numbers))
print("Odd numbers in the list:", odd_numbers)

