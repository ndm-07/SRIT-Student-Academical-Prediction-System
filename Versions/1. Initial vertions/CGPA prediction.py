def calculate_new_cgpa(current_cgpa, num_semesters, future_semesters, predictions):
    
    total_grade_points = current_cgpa * num_semesters
    
    total_grade_points += sum(predictions)
    
    new_cgpa = total_grade_points / (num_semesters + future_semesters)
    return round(new_cgpa, 2)


current_cgpa = float(input("Enter your current CGPA: "))
num_semesters = int(input("Enter the number of semesters completed: "))
future_semesters = int(input("Enter the number of future semesters to predict: "))


predictions = []
for i in range(future_semesters):
    prediction = float(input(f"Enter predicted CGPA for semester {num_semesters + i + 1}: "))
    predictions.append(prediction)


new_cgpa = calculate_new_cgpa(current_cgpa, num_semesters, future_semesters, predictions)
print("Predicted CGPA after the future semesters:", new_cgpa)
