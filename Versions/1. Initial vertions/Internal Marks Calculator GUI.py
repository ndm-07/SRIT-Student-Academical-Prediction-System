import tkinter as tk
from tkinter import messagebox

def calculate_internal_marks():
    m1 = float(mid1_entry.get())
    m2 = float(mid2_entry.get())

    if m1 > 30 or m2 > 30:
        messagebox.showinfo("Error", "Mid 30 Marks ke mawa. 30 lopala marks type chey")
        return

    if m1 >= m2:
        r1 = (m1 * 0.8) + (m2 * 0.2)
    else:
        r1 = (m2 * 0.8) + (m1 * 0.2)

    result_label.config(text="The Internal marks of MID Exams: " + str(round(r1)))

def calculate_total_internal_marks():
    m1 = float(mid1_entry.get())
    m2 = float(mid2_entry.get())
    m3 = float(caa1_entry.get())
    m4 = float(caa2_entry.get())

    if m1 > 30 or m2 > 30:
        messagebox.showinfo("Error", "Mid 30 Marks ke mawa. 30 lopala marks type chey")
        return

    if m1 >= m2:
        r1 = (m1 * 0.8) + (m2 * 0.2)
    else:
        r1 = (m2 * 0.8) + (m1 * 0.2)

    if m3 > 10 or m4 > 10:
        messagebox.showinfo("Error", "CAA 10 Marks ke swaami. 10 lopala marks type chey")
        return

    r2 = (m3 + m4) / 2
    r3 = r1 + r2

    result_label.config(text="The Internal marks along with CAA marks: " + str(round(r3)))

def predict_grade_result():
    x = int(internal_marks_entry.get())
    y = int(expected_marks_entry.get())

    if x > 40 or y > 60:
        messagebox.showinfo("Error", "Kallu Tirugutannaya? Yenni marks type chesnavo sarigga chusko.")
        return
    elif(y<21):
        messagebox.showinfo("Error", "Bro, no doubt. Fail ey. Supply ki ready ayipo.")
        return

    p = round(x) + round(y)

    if p >= 90:
        result = "You Might get S as your Grade"
    elif 80 <= p <=89:
        result = "You Might get A as your Grade"
    elif 70 <= p <=79:
        result = "You Might get B as your Grade"
    elif 60 <= p <=69:
        result = "You Might get C as your Grade"
    elif 50 <= p <=59:
        result = "You Might get D as your Grade"
    elif 40 <= p <=49:
        result = "You Might get E as your Grade"
    else:
        result = "Sorry bro. Supply ne le inka. F Grade neeku"

    result_label.config(text=result)

def on_exit():
    root.destroy()

root = tk.Tk()
root.title("Grade Calculator")

mid1_label = tk.Label(root, text="Enter Mid 1 marks:")
mid1_label.pack()
mid1_entry = tk.Entry(root)
mid1_entry.pack()

mid2_label = tk.Label(root, text="Enter Mid 2 marks:")
mid2_label.pack()
mid2_entry = tk.Entry(root)
mid2_entry.pack()

calculate_internal_button = tk.Button(root, text="Calculate Internal Marks of MID Exams", command=calculate_internal_marks)
calculate_internal_button.pack()

caa1_label = tk.Label(root, text="Enter CAA1 marks:")
caa1_label.pack()
caa1_entry = tk.Entry(root)
caa1_entry.pack()

caa2_label = tk.Label(root, text="Enter CAA2 marks:")
caa2_label.pack()
caa2_entry = tk.Entry(root)
caa2_entry.pack()

calculate_total_internal_button = tk.Button(root, text="Calculate Total Internal Marks", command=calculate_total_internal_marks)
calculate_total_internal_button.pack()

internal_marks_label = tk.Label(root, text="Enter your Internal Marks:")
internal_marks_label.pack()
internal_marks_entry = tk.Entry(root)
internal_marks_entry.pack()

expected_marks_label = tk.Label(root, text="Enter your Expected Marks in SEM Exams:")
expected_marks_label.pack()
expected_marks_entry = tk.Entry(root)
expected_marks_entry.pack()

predict_grade_button = tk.Button(root, text="Predict the Grade result of SEM Exams", command=predict_grade_result)
predict_grade_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack()

root.mainloop()
