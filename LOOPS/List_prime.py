a=[[2],[2,6,9],[8,8,7],[8,6,3]]

for i in a:
    prime = False
    for j in i:
        if j>1:
            for k in range(2,j):
                if j%k==0:
                    break
            else:
                prime = True
                break
    if prime:
        print(i)
        break


