height, number = [int(x) for x in input().split()]
pipes = [int(x) for x in input().split()]
for n in range(number-1):
    if abs(pipes[n] - pipes[n+1]) > height:
        a = 0
        print("GAME OVER")
        break
    else:
        a = 1
if a==1:
    print("YOU WIN")
    