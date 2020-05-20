x = int(input())
date = ["ano(s)", "mes(es)", "dia(s)"]
fact = [365, 30, 1]
for n,d in zip(fact,date):
    print("%d %s" %((x/n), d))
    x = x%n
