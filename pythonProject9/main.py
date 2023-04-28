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

def generate_username(birthday, phone_number, last_name):
    # Extract day, month, and year from birthday
    day, month = birthday.split("/") #https://stackoverflow.com/questions/55879461/enter-date-of-birth

    # Extract last 2 digits of phone number
    last_digits = phone_number[-2:]

    # Generate username in format: username-day month year of birthday-last digits phone number
    username = f"{last_name.lower()}{day}{month}{last_digits}@eagle.fgcu.edu"

    return username


# Get user information
birthday = input("Enter your birthday (DD/MM): ")
phone_number = input("Enter the last 2 digits of your phone number: ")
last_name = input("Enter your last name: ")

# Generate username
username = generate_username(birthday, phone_number, last_name)

print(f"Your username is: {username}")


print("Your current password is:", name + birthday + phone_number )
old_password = name + username
password = (input("Introduce a new Password: "))
if old_password != password:
    print("We have updated your password")
elif old_password == password:
    print("Your password didn't change")

security_questions = [
    "What is your mother's maiden name?",
    "What is the name of your first pet?",
    "What is your favorite book?",
]
#https://www.youtube.com/watch?v=6SifUNXKWNA
question_indices = {str(i + 1): question for i, question in enumerate(security_questions)}

#  Security Question Factor Authentication
print("Please choose a security question:")
for index, question in question_indices.items():
    print(f"{index}. {question}")

chosen_question_index = input()

# Get the user's response to the chosen security question
chosen_question = question_indices.get(chosen_question_index)

if chosen_question:
    response = input(f"Your security question is: {chosen_question}\nPlease provide the answer to this security question:")
    print(f"Your response to {chosen_question} has been saved as {response}.")
else:
    print("Invalid selection. Please choose a valid security question index.")


#Protect the password


import keyring

NAMESPACE = "my-app"
ENTRY = username

keyring.set_password(NAMESPACE, ENTRY, password)
cred = keyring.get_credential(NAMESPACE, ENTRY)


# This part of the program gives major and graduation information
#-------------------------------------------------------------
print("Now, please login with the information provided above: ")

Username = True
while Username:
    userName = (input("Enter your username: "))
    if userName == username:
        print("Now, enter your password")
        Username = False

passWord = True
while passWord:
    password_n = (input("Password: "))
    if password_n == password:
        print("Welcome", name)
        passWord = False



# Two-Factor authentication

while True:
    user_response = input(f"Please provide the answer to the security question: {chosen_question}\n")
    if user_response == response:
        print("You have been authenticated.")
        break
    else:
        print("Incorrect response. Please try again.")

print("You have successfully logged to your student account.  ")


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
