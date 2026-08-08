#a)Reading the data with error handling
def read_shelter_data(filename):
    data=[]
    try:
        with open(filename,"r") as file:
            for line in file:
                line=line.strip()
                animal=tuple(line.split(","))
                data.append(animal)
            return data
    except FileNotFoundError:
        print("File not found")
data=read_shelter_data("shelter_data.txt")
print(data)


#b)Aggregating data using a Dictionary 
def count_by_type(data):
    counts={}
    for animal in data:
        animal_type=animal[1]
        if animal_type not in counts:
            counts[animal_type]=1
        else:
            counts[animal_type]+=1  
    return counts
counts=count_by_type(data)
print("/n")
print(counts)


#c) Extracting specific data 
def not_adopted(data):
    not_adopted_list=[]
    for animal in data:
        adopted_type=animal[3]
        if adopted_type=="No":
            not_adopted_list.append(animal[0])
    return not_adopted_list
not_adopted_list=not_adopted(data)
print(not_adopted_list)


#d) Writing a report to a new file
def write_report(counts, not_adopted_list, output_filename):
    with open(output_filename, "w") as file:

        file.write("Animal Shelter Report\n\n")

        file.write("Animal Counts:\n")
        for key, value in counts.items():
            file.write(f"{key}: {value}\n")

        file.write("\nAnimals not yet adopted:\n")
        for name in not_adopted_list:
            file.write(f"{name}\n")

write_report(counts, not_adopted_list,"report.txt")




















