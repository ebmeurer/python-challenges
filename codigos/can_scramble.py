'''
Write a function that returns true if one string can be formed out of another by reordering ("scrambling") the characters.

For example:

can_scramble("abc", "cba") -> true
can_scramble("aab", "bba") -> false
'''

def can_scramble(str1, str2):
    if len(str1) != len(str2):
        return False
    while len(str1) > 1:
        if str1[0] in str2:
            index = str2.index(str1[0])
            str2 = str2[:index] + str2[index+1:]
            str1 = str1[1:]
        else:
            return False
    if str1 == str2:
        return True
    return False    
    
print(can_scramble('abc','cba'))
print(can_scramble('aab','bba'))
