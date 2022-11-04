def compareTriplets(a,b):
    alice=bob=0
    for i in range(3):
        if a[i]>b[i]:
            alice+=1
        if(a[i]<b[i]):
            bob+=1
    print(alice,bob)
arr1=[5,6,7]
arr2=[3,6,10]
compareTriplets(arr1,arr2)