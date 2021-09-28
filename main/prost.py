from math import sqrt
from datetime import datetime as dt

def cik(s,sps):
    for i in sps:
        if i <= sqrt(s):
            if s%i==0:
                s=cik(s+2,sps)
        else:
            break
    return(s)
                

def prost(s,sps):
    #sps=[2,3,5]
    while s<5200:
        s=cik(s,sps)
        sps.append(s)
        s+=2
        
    return sps

    

a=dt.now()
s=prost(7,[2,3,5])
print(s[-1])

chc1=1
for i in s[:8]:
    chc1*=i

print(int(sqrt(chc1+1)))

for i in s:
    if (chc1-1)%i==0:
        print(i)
# ch=1
# for i in s:
#     ch*=i
# print(ch+1)
# h=1
# chc=0
# while h>0:
#     ch=ch//10
#     h=ch
#     chc+=1
# print(chc)

time=f'{dt.now()-a}'
print(time)