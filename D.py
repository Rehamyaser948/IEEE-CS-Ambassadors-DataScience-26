positve_intger=abs(int(input()))
multiplication=[]
for i in range(1,11):
    result=i*positve_intger
    if result%4!=0:
        multiplication.append(result)

print(*multiplication,sep=",")












