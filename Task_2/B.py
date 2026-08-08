students_grades={"ahmed":(30,40,60),
                 "ali":(20,50,77),
                 "hana":(44,78,60),
                 "farah":(50,80,35),
                 "moatez":(65,80,45)
                 }

results={}
highest_avg_grade=[]
for key,value in students_grades.items():
    avg_grade=int(sum(value)/len(value))
    print(f"the avg grade for {key} is: {avg_grade}")
    highest_avg_grade.append(avg_grade)
    if avg_grade>=50:
        result="pass"
    else:
        result="Fail"
    results[key]=result

    highest_avg=highest_avg_grade[0]
    highest_key=""
    highest_index=0
    for i in range(len(highest_avg_grade)):  
        if highest_avg_grade[i]>highest_avg:
            highest_avg=highest_avg_grade[i]
            highest_index=i
            for j, (key, value) in enumerate(students_grades.items()):
                if j == highest_index:
                    highest_key = key

print(f"the student with the highest avg grade is {highest_key} wih avg grade {highest_avg}")           

