def CGPA_Prediction():

    num_semesters = int(input("Enter the number of semesters completed: "))
    current_cgpa = float(input("Enter your current CGPA: "))
    future_semesters = int(input("Enter the number of future semesters to predict: "))

    predictions = []
    for i in range(future_semesters):
        prediction = float(input(f"Enter predicted CGPA for semester {num_semesters + i + 1}: "))
        predictions.append(prediction)
    
    total_grade_points = current_cgpa * num_semesters
    
    total_grade_points += sum(predictions)
    
    new_cgpa = total_grade_points / (num_semesters + future_semesters)
    print("Predicted CGPA after the future semesters:", new_cgpa)


def Calculate_SGPA():
    num_subjects = int(input("Enter the number of subjects in the semester: "))
    
    total_grade_points = 0
    for i in range(num_subjects):
        grade = input(f"Enter the grade for subject {i + 1} (S, A, B, C, D, E, F): ").strip().upper()
        
        if grade == 'S':
            points = 10
        elif grade == 'A':
            points = 9
        elif grade == 'B':
            points = 8
        elif grade == 'C':
            points = 7
        elif grade == 'D':
            points = 6
        elif grade == 'E':
            points = 5
        elif grade == 'F':
            points = 0
        else:
            print("Invalid grade entered. Please enter grades as S, A, B, C, D, E, or F.")
            return
        
        total_grade_points += points
    
    # Calculate SGPA
    gpa = total_grade_points / num_subjects
    print("Your GPA for the semester is:", round(gpa, 2))

def display_menu_for_CGPA_and_SGPA_Calculation():
    print("1. To Calculate the SGPA (Semester GPA)")
    print("2. To Predict the CGPA")
    print("3. Exit")

def CGPA_and_SGPA_Calculation():
    while(True):
        display_menu_for_CGPA_and_SGPA_Calculation()
        choice = int(input("Select an option: "))
        
        if choice == 1:
            Calculate_SGPA()
            continue
        elif choice == 2:
            CGPA_Prediction()
            continue
        elif choice == 3:
            print("-----------------------------Exiting")
            break
        else:
            print("Choice Unavailable!!")
            continue

# Run the program
CGPA_and_SGPA_Calculation()