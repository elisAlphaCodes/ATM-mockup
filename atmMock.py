import datetime
import random


database = {}

def welcome():
    print("Welcome to Assurance Bank")

    # Date and Time Section1
    e = datetime.datetime.now()
    print("Current date and time:  = %s/%s/%s %s:%s:%s" % (e.day, e.month, e.year, e.hour, e.minute, e.second))

    accountUser = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))
    if (accountUser == 1):
        login()

    elif (accountUser == 2):
        register()

    else:
        print("You have selected an invalid option")
        welcome()

def login():
    print("||||||| Login Details ||||||")

    userAccount = int(input("What is your account number?: "))
    password = input("What is your password?: ")

    for accountNumber, userDetails in database.items():
        if (accountNumber == userAccount):
            if (userDetails[3] == password):
                bankOperation(userDetails)

    print('Invalid account or password')
    login()


def register():
    print("||||| Register ||||||")

    email = input("What is your email address: ")
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    password = input("create a password for yourself: ")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)

def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Complaint (4) Logout (5) Exit \n"))

    if (selectedOption == 1):

        depositOperation()
    elif (selectedOption == 2):

        withdrawalOperation()
    elif (selectedOption == 3):
        complaint()

    elif (selectedOption == 4):


        logout()
    elif (selectedOption == 5):

        exit()
    else:

        print("Invalid option selected")
        bankOperation(user)

def withdrawalOperation():
    withdraw = int(input("How much would You like to withdraw: "))
    print("Take cash %s" % withdraw)


def depositOperation():
    deposit = int(input("How much would you like to deposit: "))
    print("Current Balance %s" % deposit)

def complaint():
    input("What issue will you like to report: \n")
    print("Thank you for contacting us")


def logout():
    login()



welcome()