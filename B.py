charachter=input().lower()
essential=['a','e','i','o','u']
count=0
for i in range(len(essential)):
    for char in charachter:
        if char==essential[i]:
            count+=1


print(f"the number of = {count}")


























