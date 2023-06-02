# Python3 code to demonstrate
# checking a number is palindrome
# using str() + string slicing

# initializing number
test_number = input()
# using str() + string slicing
# for checking a number is palindrome
res = str(test_number) == str(test_number)[::-1]

# printing result
print (str(res))
