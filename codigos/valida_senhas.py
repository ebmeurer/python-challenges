'''
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''

def valida_senha(senha):
    tem_char_min = False
    tem_char_mai = False
    tem_num      = False
    tem_char_esp = False
    if len(senha) >= 6 and len(senha) <=12:
        for i in senha:
            if i.isalpha():
                if i.islower():
                    tem_char_min = True
                    continue
                if i.isupper():
                    tem_char_mai = True
                    continue
            if i in ["$","#","@"]:
                tem_char_esp = True
                continue
            if i.isnumeric():
                tem_num      = True
                continue
        if tem_char_min and tem_char_mai and tem_num and tem_char_esp:
            return True
    return False

senhas_validas = []

senhas = input("Digite as senhas a serem analisadas: ")
senhas = senhas.split(',')

for i in senhas:
    if valida_senha(i):
        senhas_validas.append(i)

print(','.join(senhas_validas))
    
