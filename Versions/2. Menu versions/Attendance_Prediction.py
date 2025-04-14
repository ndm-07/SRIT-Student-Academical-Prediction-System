def general_calculation():
    np = int(input("Enter number of periods present: "))
    tp = int(input("Enter number of total periods: "))
    att = float((np / tp) * 100)
    print("-----------------------------Your attendance is:", att)


def prediction_days_present():
    np = int(input("Enter number of periods present: "))
    tp = int(input("Enter number of total periods: "))
    x = int(input("Enter number of days to be predicted: "))
    a = np + (x * 7)
    b = tp + (x * 7)
    att = float((a / b) * 100)
    print("-----------------------------Your predicted attendance will be:", att)


def prediction_days_absent():
    np = int(input("Enter number of periods present: "))
    tp = int(input("Enter number of total periods: "))
    x = int(input("Enter number of days to be predicted: "))
    a = np
    b = tp + (x * 7)
    att = float((a / b) * 100)
    print("-----------------------------Your predicted attendance will be:", att)


def display_menu_for_Attendance_Calculator():
    print("1. General Calculation of Attendance")
    print("2. Prediction for Additional Days Present")
    print("3. Prediction for Additional Days Absent")
    print("4. Exit")


def Attendance_Calculator():
    while True:
        display_menu_for_Attendance_Calculator()
        choice = int(input("Select an option: "))
        
        if choice == 1:
            general_calculation()
        elif choice == 2:
            prediction_days_present()
        elif choice == 3:
            prediction_days_absent()
        elif choice == 4:
            print("-----------------------------Exiting")
            break
        else:
            print("Choice Unavailable!!")

Attendance_Calculator()
