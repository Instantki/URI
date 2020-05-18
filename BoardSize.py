answer = []

def condition(x, xi, y, yi):
    if x >= xi and y >= yi or x >= yi and y >= xi:
        answer.append(1)
    else:
        answer.append(0)
    pass

while True:
  try:
    inp = input().split()
    if len(inp) == 3:
        x = int(inp[0])
        y = int(inp[1])
        m = int(inp[2])
    elif len(inp) == 2:
        xi = int(inp[0])
        yi = int(inp[1])
        m -= 1
        if m>= 0:
            condition(x,xi,y,yi)
    else:
        break    
  except EOFError:
    break

for a in answer:
    if a == 1:
        print("Sim")
    else:
        print("Nao")