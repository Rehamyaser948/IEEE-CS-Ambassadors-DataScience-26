list1=[3,6,8,10,7]
list2=[6,4,5,8,9]

def common_elements (list1,list2):
    result=[]
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                result.append(list1[i])
    return(result)

print(common_elements(list1,list2))





















