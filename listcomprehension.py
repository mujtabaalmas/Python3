
# #A list is to be created of the first 15 integers, starting at 0, 
# # whose nth element is the square of the integer if it is divisible by 4, or otherwise 0
# list1 = [i**2 if i% 4 == 0 else 0 for i in range(15)]

# print("\nSquare of Integers that are divisible by 4: ",list1)

# #first nth even numbers 
# evens = [i for i in range(20) if i % 2 == 0]
# print("First Nth Even numbers: ",evens)

# # printing cube of first 10 even numbers 
# evens_cube = [i**3 for i in range(20) if i % 2 ==0 ]
# print("Cube of even Numbers: ",evens_cube)

# #finding remainder of two lists by mergings two lists and printing both by single expression
# a = [10, 5, 51]
# b = [30, 9,7]
# a.extend(b)
# print("\nlist A and B Values")
# for num in a:
#     print(num, '%', 2, '=', num % 2)


#Removing / adding Elements from list
number_list = [10, 20, 30, 40, 70, 89, 46, 64, 67]
print("\nOriginal List: ",number_list)
user_choice = input("Add Elements to Existing list: Yes / No (Y/N): ")
if user_choice in ('Y', 'y', 'Yes', 'yes'):
    user_add_choice = int(input("How many Elements do you want to add: "))
    if user_add_choice <= 0:
        print(f"Cannot Add that number of element/s: {user_add_choice}")
        raise StopIteration
    else:
        for i in range(user_add_choice):
            element = int(input(f"Enter element no. {i+1}: "))
            number_list.append(element)
elif user_choice in ('N', 'n', 'No', 'no'):
    print("No elements added to the list.")
else:
    print("Invalid input.")
    raise SystemExit

print("\nUpdated List:", number_list)

okgoogle = int(input("No. of elements you want to remove from list: (1-9): "))
for i in range(okgoogle):
    valuefromuser = int(input(f"Enter element {i+1} to remove: "))
    if valuefromuser in number_list:
        number_list.remove(valuefromuser)
        print(f'Removed {valuefromuser}')
    else:
        print(f'{valuefromuser} not found in list.')
    print('List:', number_list)

    
