x , y = [float(x) for x in input().split()]
a, b = [float(x) for x in input().split()]
z = ((a - x)**2 + (b - y)**2)**(1/2)

print("%.4f" %z)