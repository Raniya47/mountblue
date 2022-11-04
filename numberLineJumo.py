def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1<x2 and v1<v2:
        print("NO")
    else:
        if v1!=v2 and (x2-x1)%(v2-v1)==0:
            print("YES")
        else:
            print("NO")
kangaroo(0, 3, 4, 5)