A,B,C = [int(x) for x in input().split()]

maiorAB = (A + B + abs(A-B)) / 2
maiorAC = (maiorAB + C + abs(maiorAB-C)) / 2

print ("%d eh o maior" %maiorAC)