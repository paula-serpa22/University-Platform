""""Gives information about the program
"""
# Maria Paula Serpa Sanchez
# Students can use this program to know more information about credits, graduation, requirements, financial aid.
# The student has to create and account and login to it to receive the information#
print("Welcome to your FGCU Student portal")


def print_message(slogan_to_print):
    """Show to the student the University's slogan
        """

    print("Your", slogan_to_print, "here!")


def main():
    """Show to the student the University's slogan
    """
    future_student = "Future begins"
    print_message(future_student)
    print_message("Dreams begin")
    print_message("Aspirations begin")


main()
print("Wings Up!")
# This part of the program asks information to the student
# It creates an username and password based on the information
print("Create your student account")
name = input("Enter your name: ")
print("Welcome", name + ".")
Id = input("Enter the last 4 digits of your id number: ")
print("Your full ID number is 9832" + Id)
print("Your username is: ", name + "_" + Id)
UserName = input("Please enter the username based on the information provided above: ")
Phone = input("Enter the last 4 digits of  your phone number: ")
print("Your current password is:", name + Id + Phone)
old_password = name + Id + Phone
password = (input("Introduce a new Password: "))
if old_password != password:
    print("We have updated your password")
elif old_password == password:
    print("Your password didn't change")

print("Now, please login with the information provided above: ")

Username = True
while Username:
    username = (input("Enter your username: "))
    if username == UserName:
        print("Now, enter your password")
        Username = False

passWord = True
while passWord:
    password_n = (input("Password: "))
    if password_n == password:
        print("Welcome", name)
        passWord = False

print("You have successfully logged to your student account.  ")

# This part of the program gives major and graduation information
print("Now, you will receive information about your graduation")
Major = input("Please enter your major: ")
while True:

    try:

        grad = int(input("Please enter your year of graduation: "))

        break

    except ValueError:

        print("Error. Must be a whole number.")
Year = input("Enter current year: ")

while True:

    try:

        year = int(input("Please enter your year of graduation: "))

        break

    except ValueError:

        print("Error. Must be a whole number.")

graduation = grad - year
print("You will graduate in", graduation, "years in", Major + ".")
# This part of the program calculates the number of  Credits per semester the student will take
Credit = input("How many credits do you have to take to graduate?: ")
Credits = int(Credit)
currently = input("How many credits have you taken so far?: ")
current_credit = int(currently)
credits_to_take = Credits - current_credit
print("You still have to take", credits_to_take, "credits. ")
cred_semester = graduation * 2
credit_semester = credits_to_take / cred_semester
print("To graduate in", graduation, "years,", "you will have to take", credit_semester, "credits per semester.")

# Center for Academic Achievement survey
print("Center for Academic Achievement ask you to answer the following survey")
col_year = input("Which year are you in college? Freshman, sophomore, junior or senior:")
subjects = input("Please enter the subjects you are currently taking,separate them with commas: ")
print(name, "is currently taking", subjects)
Hours = input("please enter the number of hours you spend studying weekly:")
hours = int(Hours)
Hours_col = input("Enter the number of hours you spend attending to classes, at campus or online:")
hours_col = int(Hours_col)
timeCollege = hours + hours_col
print(name, "spend", timeCollege, "hours in activities related with college.")


# This part of the program compares the lowest score from two subjects


def getSmaller(subject1_grade, subject2_grade):
    """

    :param subject1_grade:
    :param subject2_grade:
    :return:
    """
    if subject1_grade < subject2_grade:
        smaller = subject1_grade
    else:
        smaller = subject2_grade
    return smaller


def main():
    """it takes data and give recommendations
    """
    print("Please enter the grade of two subjects in which you are struggling with")
    subject1_grade = int(input("First subject's Grade: "))
    subject2_grade = int(input("Second subject's Grade: "))

    smaller_number = getSmaller(subject1_grade, subject2_grade)
    print("What is the name of the subject in which your grade is", smaller_number, "?")
    subject_lowest_grade = input("Enter the subject's name: ")
    print("To improve your grade in", subject_lowest_grade + ",", "you should talk with you professor.")
    print("Also, you should schedule an appointment with an Academic Advisor")


print("frequent questions: ")
advisor = True
professor = True
print("Talking to my teacher and an advisor will help me improve my grades?")
print(advisor and professor)
print("Could just talking to one of them help me improve my grades?")
print(advisor or professor)
print("If I do nothing, I will probably pass the courses")
print(not professor)

main()

# This part of the program calculates the amount of money the student has to pay

# Financial Aid Center Survey
print("Financial Aid Center ask you to answer the following survey")
Money = input("How much are you paying for the current semester?: ")
money = float(Money)
F_A = input("How much financial aid are you receiving?: ")
f_a = float(F_A)
pay = money - f_a
print("You have to pay: $", format(pay, ".2f"), sep='')

number_of_subjects = int(input("How many subjects are you taking during the current semester?: "))
total = 0
print("Enter the number of books you have to buy (One line per subject)")
for x in range(number_of_subjects):
    books = int(input("Number of books: "))
    total += books
print("During the current semester you have to buy", total, "books")

print("Do you have enough money to pay college (including books' costs?")
answer = input("Please type yes or no: ")
answer = answer.lower()
if answer == "yes":
    print("Congratulations!")
else:
    print("Please visit the Financial Aid department for scholarship's opportunities.")
print("Have a good Day!")
