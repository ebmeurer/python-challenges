'''
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''
from math import sqrt

posicao = [0,0]
instrucoes = []
a = True

while a:
    a = input()
    if a:
        instrucoes.append(a)

for i in instrucoes:
    side, distance = i.split(" ")[0], i.split(" ")[1]
    
    if side.upper() == "UP":
        posicao[0] += int(distance)
        continue
    
    if side.upper() =="DOWN":
        posicao[0] -= int(distance)
        continue
    
    if side.upper() =="LEFT":
        posicao[1] -= int(distance)
        continue
    
    if side.upper() =="RIGHT":
        posicao[1] += int(distance)
        continue

#calcula o quadrado dos catetos
total_distance = pow(posicao[0],2)+pow(posicao[1],2)

#calcula e arredonda a hipotenusa, que representa a distancia percorrida do ponto inicial ao final
total_distance = int(round(sqrt(total_distance)))

print (total_distance)
