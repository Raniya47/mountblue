def quickSort(ar):
    mid,left,right=[],[],[]
    mid.append(ar[0])
    for i in range(len(ar)):
        if (ar[i]<ar[0]):
            left.append(ar[i])
        if ar[i]>ar[0]:
            right.append(ar[i])
    print(left+mid+right)
    # print(mid)

arr=[5,7,4,3,8]
quickSort(arr)