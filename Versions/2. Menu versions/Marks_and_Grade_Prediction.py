def calculate_internal_marks():
    m1 = float(input("Enter Mid 1 marks: "))
    m2 = float(input("Enter Mid 2 marks: "))
    
    if m1 > 30 or m2 > 30:
        print("--------Mid marks should be within 30. Please enter valid marks.")
        return
    
    if m1 >= m2:
        r1 = (m1 * 0.8) + (m2 * 0.2)
    else:
        r1 = (m2 * 0.8) + (m1 * 0.2)
    
    print("--------The Internal marks of MID Exams:", round(r1))


def calculate_total_internal_marks():
    m1 = float(input("Enter Mid 1 marks: "))
    m2 = float(input("Enter Mid 2 marks: "))
    m3 = float(input("Enter CAA1 marks: "))
    m4 = float(input("Enter CAA2 marks: "))
    
    if m1 > 30 or m2 > 30:
        print("--------Mid marks should be within 30. Please enter valid marks.")
        return

    if m1 >= m2:
        r1 = (m1 * 0.8) + (m2 * 0.2)
    else:
        r1 = (m2 * 0.8) + (m1 * 0.2)

    print("--------The Internal marks of MID Exams:", round(r1))

    if m3 > 10 or m4 > 10:
        print("--------CAA marks should be within 10. Please enter valid marks.")
        return

    r2 = (m3 + m4) / 2
    r3 = r1 + r2
    print("--------The Internal marks along with CAA marks:", round(r3))


def predict_grade():
    x = int(input("Enter your Internal Marks: "))
    y = int(input("Enter your Expected Marks in SEM Exams: "))
    
    if x > 40 or y > 60:
        print("--------Marks should be within limits (Internal <= 40, SEM <= 60). Please enter valid marks.")
        return
    
    if y < 21:
        print("--------Sorry, insufficient marks. Likely a fail.")
        return
    
    total_marks = x + y
    
    if total_marks >= 90:
        grade = "S"
    elif total_marks >= 80:
        grade = "A"
    elif total_marks >= 70:
        grade = "B"
    elif total_marks >= 60:
        grade = "C"
    elif total_marks >= 50:
        grade = "D"
    elif total_marks >= 40:
        grade = "E"
    else:
        grade = "F"
    
    print(f"--------You might get {grade} as your Grade")


def display_menu_for_Marks_and_Grade_Calculation():
    print("1. To Calculate Internal Marks of MID Exams")
    print("2. To Calculate Total Internal Marks")
    print("3. To Predict the Grade of SEM Exams")
    print("4. Exit")


def Marks_and_Grade_Prediction():
    while True:
        display_menu_for_Marks_and_Grade_Calculation()
        choice = int(input("Select an option: "))
        
        if choice == 1:
            calculate_internal_marks()
            continue
        elif choice == 2:
            calculate_total_internal_marks()
            continue
        elif choice == 3:
            predict_grade()
            continue
        elif choice == 4:
            print("--------Exiting")
            break
        else:
            print("--------Invalid choice. Please select a valid option.")
            continue


# Run the program
Marks_and_Grade_Prediction()

