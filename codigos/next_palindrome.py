'''
Given a number, find the next smallest palindrome larger than the number. For example if the number is 125, next smallest palindrome is 131.
'''

def find_palindrome(num):
    next_num = num + 1
    while True:
        if str(next_num) == str(next_num)[::-1]:
            return next_num
        next_num += 1
    
print(find_palindrome(125))
