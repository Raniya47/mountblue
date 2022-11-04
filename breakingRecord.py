def breakingRecord(score):
    mini=maxi=score[0]
    mincount=maxcount=0
    for i in range(len(score)):
        if score[i]>maxi:
            maxi=score[i]
            maxcount+=1
        if score[i]<mini:
            mini=score[i]
            mincount+=1
    print(maxcount,mincount)

scores=[3,4,21,36,10,28,35,5,24,42]
breakingRecord(scores)