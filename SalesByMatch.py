def sockMerchant(n,ar):
    count=0
    for i in range(0,n):
        dup=1
        for j in range(i+1,n):
            if ar[i]==None:
                continue
            if ar[i]==ar[j] and dup==1:
                count+=1
                dup+=1
                ar[j]=None
    print(count)
arr=[1,2,1,2,1,2,2]
num=len(arr)
sockMerchant(num,arr)