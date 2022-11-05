def superReducedString(str):
    arr=[]
    count=0
    res=[]
    for i in range(len(str)):
        arr.append(str[i])
    n=len(arr)
    for i in range(0,n):
        dup=1
        for j in range(i+1,n):
            if arr[i]==None:
                continue
            if arr[i]==arr[j] and dup==1:
                count+=1
                dup+=1
                # temp.append(arr[i])
                # temp.append(arr[j])
                arr[j]=None
                arr[i]=None
            else:
                res.append(arr[i])
    # print(arr)
    # print(count)   
    # print(temp)
    # print(res)
    result=''
    for i in range(len(arr)):
        if(arr[i]!=None):
            result+=arr[i]
    print(result)   
str="I looveee yooouuu Mistii"
superReducedString(str)