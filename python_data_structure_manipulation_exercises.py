#20 Python Data Structure Manipulation Exercises

#The following questions reference the students data structure below. Write the python code to answer the following questions:

students = [
    {
"id": "100001",
"student": "Ada Lovelace",
"coffee_preference": "light",
"course": "web development",
"grades": [70, 91, 82, 71],
"pets": [{"species": "horse", "age": 8}],
    },
    {
"id": "100002",
"student": "Thomas Bayes",
"coffee_preference": "medium",
"course": "data science",
"grades": [75, 73, 86, 100],
"pets": [],
    },
    {
"id": "100003",
"student": "Marie Curie",
"coffee_preference": "light",
"course": "web development",
"grades": [70, 89, 69, 65],
"pets": [{"species": "cat", "age": 0}],
    },
    {
"id": "100004",
"student": "Grace Hopper",
"coffee_preference": "dark",
"course": "data science",
"grades": [73, 66, 83, 92],
"pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
"id": "100005",
"student": "Alan Turing",
"coffee_preference": "dark",
"course": "web development",
"grades": [78, 98, 85, 65],
"pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
"id": "100006",
"student": "Rosalind Franklin",
"coffee_preference": "dark",
"course": "data science",
"grades": [76, 70, 96, 81],
"pets": [],
    },
    {
"id": "100007",
"student": "Elizabeth Blackwell",
"coffee_preference": "dark",
"course": "web development",
"grades": [69, 94, 89, 86],
"pets": [{"species": "cat", "age": 10}],
    },
    {
"id": "100008",
"student": "Rene Descartes",
"coffee_preference": "medium",
"course": "data science",
"grades": [87, 79, 90, 99],
"pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
"id": "100009",
"student": "Ahmed Zewail",
"coffee_preference": "medium",
"course": "data science",
"grades": [74, 99, 93, 89],
"pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
"id": "100010",
"student": "Chien-Shiung Wu",
"coffee_preference": "medium",
"course": "web development",
"grades": [82, 92, 91, 65],
"pets": [{"species": "cat", "age": 8}],
    },
    {
"id": "100011",
"student": "William Sanford Nye",
"coffee_preference": "dark",
"course": "data science",
"grades": [70, 92, 65, 99],
"pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
"id": "100012",
"student": "Carl Sagan",
"coffee_preference": "medium",
"course": "data science",
"grades": [100, 86, 91, 87],
"pets": [{"species": "cat", "age": 10}],
    },
    {
"id": "100013",
"student": "Jane Goodall",
"coffee_preference": "light",
"course": "web development",
"grades": [80, 70, 68, 98],
"pets": [{"species": "horse", "age": 4}],
    },
    {
"id": "100014",
"student": "Richard Feynman",
"coffee_preference": "medium",
"course": "web development",
"grades": [73, 99, 86, 98],
"pets": [{"species": "dog", "age": 6}],
    },
]


#How many students are there?

print(len(students))

#How many students prefer light coffee? For each type of coffee roast?

light_coffee = 0
medium_coffee = 0
dark_coffee = 0

for i in students:
    if i ["coffee_preference"] == "light":
        light_coffee += 1
    elif i ["coffee_preference"] == "meidum":
        medium_coffee += 1
    else:
        dark_coffee += 1

print('Number of student that prefer light coffee:', light_coffee, "students")

#How many types of each pet are there?

species_dog = 0
species_cat = 0
species_horse = 0

for i in students:
    lst = i["pets"]
    if len(lst) > 0:
        for num_species in range (len(lst)):
            if lst[num_species]["species"] == "dog":
                species_dog += 1
            elif lst[num_species]["species"] == "cat":
                species_cat += 1
            else:
                species_horse += 1

print("Number of pets:", species_dog, "dogs")

#How many grades does each student have? Do they all have the same number of grades?



#What is each student's grade average?

for i in students:
    avg_grades = sum(i["grades"]) / len(i["grades"])
    print (i["student"], avg_grades)

#How many pets does each student have?
#How many students are in web development? data science?
#What is the average number of pets for students in web development?
#What is the average pet age for students in data science?
#What is most frequent coffee preference for data science students?
#What is the least frequent coffee preference for web development students?
#What is the average grade for students with at least 2 pets?
#How many students have 3 pets?
#What is the average grade for students with 0 pets?
#What is the average grade for web development students? data science students?
#What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
#What is the average number of pets for medium coffee drinkers?
#What is the most common type of pet for web development students?
#What is the average name length?
#What is the highest pet age for light coffee drinkers?