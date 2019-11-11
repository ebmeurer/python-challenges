'''
Given a number, find the next higher number using only the digits in the given number. For example if the given number is 1234, next higher number with same digits is 1243.
'''

def find_same_digits(num):
    next_num = num + 1
    str_num = str(num)
    while True:
        #checa se ainda é possível encontrar ouro numero com os mesmos digitos
        if len(str_num) !=  len(str(next_num)):
            return False
        if compara_num(str(num),str(next_num)):
            return next_num
        next_num += 1
        
def compara_num(num1, num2):
    if len(num1) != len(num2):
        return False
    while len(num1) > 1:
        if num1[0] in num2:
            index = num2.index(num1[0])
            num2 = num2[:index] + num2[index+1:]
            num1 = num1[1:]
        else:
            return False
    if num1 == num2:
        return True
    return False    
    
print(find_same_digits(1234))
