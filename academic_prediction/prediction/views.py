from django.shortcuts import render
from django.http import HttpResponse

# Attendance Prediction
def attendance_prediction(request):
    context = {}

    if request.method == "POST":
        # Retrieve the selected choice, present periods, and total periods from the form
        choice = int(request.POST.get('choice'))
        np = int(request.POST.get('present_periods'))
        tp = int(request.POST.get('total_periods'))

        # Store the form inputs in the context to maintain state across form submissions
        context.update({
            'choice': choice,
            'present_periods': np,
            'total_periods': tp,
        })

        # Process based on the choice and additional inputs
        if 'next' in request.POST:
            # Step 1: Display additional fields if needed
            if choice == 1:
                # General calculation does not need further input
                att = (np / tp) * 100
                context['attendance'] = round(att, 2)
            elif choice == 2:
                # Show input for additional days present
                context['show_days_present'] = True
            elif choice == 3:
                # Show input for additional days absent
                context['show_days_absent'] = True

        elif 'calculate' in request.POST:
            # Step 2: Perform the calculations based on user's second input
            if choice == 2 and 'days_present' in request.POST:
                days_present = int(request.POST.get('days_present'))
                a = np + (days_present * 7)
                b = tp + (days_present * 7)
                att = (a / b) * 100
                context['attendance'] = round(att, 2)
                context['days_present'] = days_present

            elif choice == 3 and 'days_absent' in request.POST:
                days_absent = int(request.POST.get('days_absent'))
                a = np
                b = tp + (days_absent * 7)
                att = (a / b) * 100
                context['attendance'] = round(att, 2)
                context['days_absent'] = days_absent

    return render(request, 'attendance.html', context)






# Marks and Grade Prediction
def marks_prediction(request):
    context = {}

    if request.method == "POST":
        choice = int(request.POST.get('choice', 0))
        
        # Handle Choice 1: Calculate Internal Marks
        if choice == 1:
            m1 = float(request.POST.get('mid1_marks',0))
            m2 = float(request.POST.get('mid2_marks',0))
            if m1 > 30 or m2 > 30:
                context['error_message'] = "Mid marks should be within 30"
            else:
                internal_marks = (m1 * 0.8) + (m2 * 0.2) if m1 >= m2 else (m2 * 0.8) + (m1 * 0.2)
                context['internal_marks'] = round(internal_marks)
            context['choice'] = choice
        
        # Handle Choice 2: Calculate Total Internal Marks
        elif choice == 2:
            m1 = float(request.POST.get('mid1_marks', 0))
            m2 = float(request.POST.get('mid2_marks', 0))
            caa1 = float(request.POST.get('caa1_marks', 0))
            caa2 = float(request.POST.get('caa2_marks', 0))

            if m1 > 30 or m2 > 30:
                context['error_message'] = "Mid marks should be within 30"
            elif caa1 > 10 or caa2 > 10:
                context['error_message'] = "CAA marks should be within 10"
            else:
                internal_marks = (m1 * 0.8) + (m2 * 0.2) if m1 >= m2 else (m2 * 0.8) + (m1 * 0.2)
                caa_avg = (caa1 + caa2) / 2
                total_internal_marks = internal_marks + caa_avg
                context['total_internal_marks'] = round(total_internal_marks)
            context['choice'] = choice

        # Handle Choice 3: Predict Grade
        elif choice == 3:
            internal_marks_input = int(request.POST.get('internal_marks_input',-1))
            sem_marks_input = int(request.POST.get('sem_marks_input',-1))
            
            if internal_marks_input > 40 or sem_marks_input > 60:
                context['error_message'] = "Marks should be within limits (Internal <= 40, SEM <= 60)"
            else:
                total_marks = internal_marks_input + sem_marks_input
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
                elif total_marks >= 0:
                    grade = "F"
                else:
                    grade = ''
                context['grade'] = grade
            context['choice'] = choice

    # If GET request, reset to initial state
    return render(request, 'marks.html', context)






def sgpa_prediction(request):
    num_subjects = 0
    grades = []
    sgpa = None
    show_grade_inputs = False

    if request.method == "POST":
        if 'calculate' in request.POST:
            # Final submission: Calculate the SGPA
            num_subjects = int(request.POST.get('num_subjects', 0))
            total_grade_points = 0

            # Retrieve grades entered for each subject
            for i in range(1, num_subjects + 1):
                grade = request.POST.get(f'grade_{i}').upper()
                points = 0
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
                
                total_grade_points += points
            
            # Calculate SGPA
            calculated_sgpa = total_grade_points / num_subjects if num_subjects > 0 else 0
            sgpa = round(calculated_sgpa,2)

        else:
            # Initial submission to get the number of subjects
            num_subjects = int(request.POST.get('num_subjects', 0))

            # Prepare for the next stage: collecting grades for each subject
            show_grade_inputs = True
            grades = range(1, num_subjects + 1)

    return render(request, 'sgpa.html', {
        'sgpa': sgpa,
        'subjects': grades,
        'show_grade_inputs': show_grade_inputs,
        'num_subjects': num_subjects,
    })



def cgpa_prediction(request):
    num_semesters = 0
    current_cgpa = 0.0
    future_semesters = 0
    predictions = []
    predicted_cgpa = None
    show_prediction_inputs = False

    if request.method == "POST":
        # Check if it's the initial or final form submission
        if 'calculate' in request.POST:
            # Final submission: Calculate the CGPA
            num_semesters = int(request.POST.get('num_semesters', 0))
            current_cgpa = float(request.POST.get('current_cgpa', 0.0))
            future_semesters = int(request.POST.get('future_semesters', 0))

            # Retrieve predicted CGPAs from stored inputs
            predictions = [float(request.POST.get(f'predicted_cgpa_{i+1}', 0.0)) for i in range(future_semesters)]
            
            # Calculate the predicted CGPA
            total_grade_points = current_cgpa * num_semesters + sum(predictions)
            predicted = total_grade_points / (num_semesters + future_semesters) if (num_semesters + future_semesters) > 0 else current_cgpa
            predicted_cgpa = round(predicted,2)

        else:
            # Initial submission to get number of future semesters
            num_semesters = int(request.POST.get('num_semesters', 0))
            current_cgpa = float(request.POST.get('current_cgpa', 0.0))
            future_semesters = int(request.POST.get('future_semesters', 0))

            # Prepare for the second form stage by setting up placeholders for inputs
            show_prediction_inputs = True
            predictions = range(future_semesters)

    return render(request, 'cgpa.html', {
        'predicted_cgpa': predicted_cgpa,
        'predicted_semesters': predictions,
        'show_prediction_inputs': show_prediction_inputs,
        'num_semesters': num_semesters,
        'current_cgpa': current_cgpa,
        'future_semesters': future_semesters,
    })








def index(request):
    return render(request, 'index.html')