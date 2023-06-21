def GetYourDay(Uinput):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    RNum = [1, 2, 3, 4, 5, 6, 7]

    # Using if-else Condition
    if Uinput in RNum:
        print("Assignment 1 - Printing Using if-else:"+days[Uinput - 1])
    else:
        print('You selected out of range')

    # Using Match-case(it only runs with 3.10 python version)
    match Uinput:
        case Uinput if Uinput in RNum:
            print("Assignment 2 - Printing Using Match-case:"+days[Uinput - 1])
        case _:
            print('You selected a number out of range.')

def RankMyScore(MarksInput):
    print("Assignment 3 - ------Printing Using Nested-if:--------")
    if MarksInput > 35:
        if MarksInput > 60:
            if MarksInput > 75:
                print('You Scored DISTINCTION !!!')
            else:
                print('You Scored FIRST CLASS !!')
        else:
            print('You Scored SECOND-CLASS !')
    else:
        print('Sorry !!! You FAILED.')


    print("Assignment 4 - ------Printing Using Match-case:--------")
    match MarksInput:
        case MarksInput if MarksInput > 75:
            print('You Scored DISTINCTION !!!')
        case MarksInput if MarksInput > 60:
            print('You Scored FIRST CLASS !!')
        case MarksInput if MarksInput > 35:
            print('You Scored SECOND-CLASS !')
        case MarksInput if MarksInput < 35:
            print('Sorry !!! You FAILED.')


def GetMonth(Month):
    print("Assignment 5 -------Printing Using if-elif-----------")

    if Month == "jan":
        print("January")
    elif Month == "feb":
        print("February")
    elif Month == "mar":
        print("March")
    elif Month == "apr":
        print("April")
    elif Month == "may":
        print("May")
    elif Month == "jun":
        print("June")
    elif Month == "jul":
        print("July")
    elif Month == "aug":
        print("August")
    elif Month == "sep":
        print("September")
    elif Month == "oct":
        print("October")
    elif Month == "nov":
        print("November")
    elif Month == "dec":
        print("December")
    else:
        print("There is no month like you selected!!")

    print("Assignment 6 --------Printing Using Match-case:--------")
    match Month:
        case "jan":
            print("January")
        case "feb":
            print("February")
        case "mar":
            print("March")
        case "apr":
            print("April")
        case "may":
            print("May")
        case "jun":
            print("June")
        case "jul":
            print("July")
        case "aug":
            print("August")
        case "sep":
            print("September")
        case "oct":
            print("October")
        case "nov":
            print("November")
        case "dec":
            print("December")
        case _:
            print("There is no month like you selected!!")


while True:
    print("///////////////////////////////////////////////////")
    FunCh = int(input("""Select a option to choose a operation[1/2/3]:
    1. Print Weekday using numer
    2. Know your rank with your Marks
    3. Print Month name with first 3 letters
    """))
    match FunCh:
        case 1:
            Uinput = int(input('Enter a Number in from 1-7:'))
            GetYourDay(Uinput)
        case 2:
            MarksInput = int(input("Enter Marks you Scored:"))
            RankMyScore(MarksInput)
        case 3:
            Month = input("Enter first 3 letters of month:").lower()
            GetMonth(Month)


