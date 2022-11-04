n=4
for i in range(n):
    # print(i)
    for j in range(n+1):
        if i+j>n-1:
        # if i+j>=n-1:
            print("#",end="")
        if(i+j<n-1):
        # else:
            print(" ",end="")
    print("\r")
   