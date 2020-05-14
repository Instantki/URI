pi = 3.14159
A,B,C = [float(x) for x in input().split()]
trianglerect = (A*C) / 2
circle = pi * C**2
trapezium = ((A+B) * C) / 2
square = B**2
rectangle = A*B

print ("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f" %(trianglerect,circle,trapezium, square, rectangle))