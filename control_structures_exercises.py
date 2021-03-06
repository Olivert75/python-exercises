#Conditional Basics

#prompt the user for a day of the week, print out whether the day is Monday or not

user_input = input('What day is today?').lower()

if user_input != 'monday':
    print ('It is not Monday')
else:
    print ("Yay!!! Happy Monday")

#prompt the user for a day of the week, print out whether the day is a weekday or a weekend

user_input = input('What day is today?').lower() 

if user_input in ["saturday", "sunday"]:
    print("Finally It's the Weekend!")
else:
    print('It is a weekday')

#create variables and make up values for
#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hrs_per_week = 38
hourly_rate = 30
over_time = 0

if hrs_per_week > 40:
    over_time = (hrs_per_week - 40) * (hourly_rate / 2)
    print(hrs_per_week * hourly_rate + over_time)
else:
    print(hrs_per_week * hourly_rate)

#Loop Basics

#While

#Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.
#Your output should look like this:
#5
#6
#7
#8
#9
#10
#11
#12
#13
#14
#15

i = 5
while i <= 15:
    i += 1
    print(i)

#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    i += 2
    print(i)

#Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -5:
    i -= 5
    print(i)

#Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
 #2
 #4
 #16
 #256
 #65536

i = 2
while i < 1000000:
    i **= 2
    print (i)

#Write a loop that uses print to create the output shown below.
#100
#95
#90
#85
#80
#75
#70
#65
#60
#55
#50
#45
#40
#35
#30
#25
#20
#15
#10
#5

i = 100
while i > 0:
    i -= 5
    print(i)

#For Loops

#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

#For example, if the user enters 7, your program should output:
#7 x 1 = 7
#7 x 2 = 14
#7 x 3 = 21
#7 x 4 = 28
#7 x 5 = 35
#7 x 6 = 42
#7 x 7 = 49
#7 x 8 = 56
#7 x 9 = 63
#7 x 10 = 70

num_input = int(input("Please enter a whole number: "))

for i in range (1, 11):
    result = i * num_input
    print(f'{i} X {num_input} = {result}')

#Create a for loop that uses print to create the output shown below.
#1
#22
#333
#4444
#55555
#666666
#7777777
#88888888
#999999999

for i in range (1,10):
    print (i * str(i))


#break and continue

#Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
#Your output should look like this:
#Number to skip is: 27

#Here is an odd number: 1
#Here is an odd number: 3
#Here is an odd number: 5
#Here is an odd number: 7
#Here is an odd number: 9
#Here is an odd number: 11
#Here is an odd number: 13
#Here is an odd number: 15
#Here is an odd number: 17
#Here is an odd number: 19
#Here is an odd number: 21
#Here is an odd number: 23
#Here is an odd number: 25
#Yikes! Skipping number: 27
#Here is an odd number: 29
#Here is an odd number: 31
#Here is an odd number: 33
#Here is an odd number: 35
#Here is an odd number: 37
#Here is an odd number: 39
#Here is an odd number: 41
#Here is an odd number: 43
#Here is an odd number: 45
#Here is an odd number: 47
#Here is an odd number: 49

while True:
    num = input("please enter a number")
    if num.isdigit():
        if int(num) % 2 != 0 and int(num) <=50:
            break
        
num = int(num)

for i in range (1, 50, 2):
    if i == num:
        print("Yikes! Skipping number:", num)
    else: 
        print ("Here is an odd number: ", i)

#The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#(Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

while True:
    num = int(input("Please enter a positive number:  "))
    if num > 0:
        break
for i in range (0, num + 1):
    print(i)

#Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

while True:
    num = input("Please enter a positive number:  ")
    if num.isdigit () and  int(num) > 0:
        break

for i in range (int(num), 0, -1):
    print (i)

#Fizzbuzz

#One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
#Write a program that prints the numbers from 1 to 100.
#For multiples of three print "Fizz" instead of the number
#For the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)

#Display a table of powers.

#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.
#What number would you like to go up to? 5
#Bonus: Research python's format string specifiers to align the table
#Here is your table!
#number | squared | cubed
#------ | ------- | -----
#1      | 1       | 1
#2      | 4       | 8
#3      | 9       | 27
#4      | 16      | 64
#5      | 25      | 125

while True: 
    try:
        num = input("Please enter a number: ")
        if num.isdigit:
            print (f'Number | Squared | Cubed')
            print(f'------ | ------- | -----')
            for i in range (-1, int(num) + 1):
                print(f'{i:<6} | {i**2:<7} | {i**3:<5}')
            if input("Do you want to continue: Y/N ?").lower() in ["yes", "y"]:
                continue
            else:
                break
    except(ValueError):
        raise Exception("Sorry, you weren't enter a number")

#Convert given number grades into letter grades.

#Prompt the user for a numerical grade from 0 to 100.
#Display the corresponding letter grade.
#Prompt the user to continue.
#Assume that the user will enter valid integers for the grades.
#The application should only continue if the user agrees to.
#Grade Ranges:

#A : 100 - 88
#B : 87 - 80
#C : 79 - 67
#D : 66 - 60
#F : 59 - 0
#Bonus

#Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
while True:
    try:
        grade = input("Enter a numerical grade: ")
        letter_grade = ["A", "B", "C", "D", "F"]
        print ("Grade Range: ")
        if grade.isdigit and 0 <=  int(grade) <= 100:
            if int(grade) >= 88 and int(grade) <= 100:
                print(f'{letter_grade[0]} : {grade}')
            elif int(grade) >= 80 and int(grade) <= 87:
                print(f'{letter_grade[1]} : {grade}')
            elif int(grade) >= 67 and int(grade) <= 79:
                print(f'{letter_grade[2]} : {grade}')
            elif int(grade) >= 60 and int(grade) <= 66:
                print(f'{letter_grade[-2]} : {grade}')
            else:
                print(f'{letter_grade[-1]} : {grade}')
            if input("Do you want to continue: Y/N ?").lower() in ["yes", "y"]:
                continue
            else:
                break
    except(ValueError): 
        break

#Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. 
#Loop through the list and print out information about each book.
#Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

books = [
    {"Title" : "The hobbit, or There and Back Again",
    "Author" : "J.R.R.Tolkien",
    "Genre" : "fantasy fiction"},

    {"Title" : "to kill a mockingbird",
    "Author" : "harper lee",
    "Genre" : "thriller"},

    {"Title" : "the help",
    "Author" : "kathryn stockett",
    "Genre" : "historical fiction"}
]

book_genre = input("Enter a genre you like").lower()
genre_lst = []

#Append the all the genre in books into genre list
for i in books:
    genre_lst.append(i["Genre"])

#Look into the list for specific genre
while True:
    if book_genre.lower() in genre_lst:
        print(i["Title"].lower())
        break
    else:
        print("No books in that genre, try something else")
        break