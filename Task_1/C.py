word=input("enter the word:")

repeated=[]
found= "All Unique"
for w in word:
    if w not in repeated:
        repeated.append(w) 
       
    else:
        found="Has Repeats"
        break

print(found)

















