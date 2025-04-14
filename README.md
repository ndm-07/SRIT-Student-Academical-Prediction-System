# 🎓 Academic Performance Prediction System using Django

A Django-based web application designed to predict and analyze various academic parameters such as **CGPA, SGPA, Attendance, Marks, and Grades**. It follows SRIT (Srinivasa Ramanujan Institute of Technology) protocols and provides an intuitive interface with Bootstrap-styled UI and interactive modals.

---

## 🔧 Software Configuration

### 1. Python Installation

- Download Python 3.7.6: [Official Download Page](https://www.python.org/downloads/release/python-376/)
- During installation:
  - ✅ Check **"Add Python to PATH"**
  - Click **Install Now**
- Verify installation:
  ```bash
  python --version
  ```
  Should display: `Python 3.7.6`

---

### 2. Virtual Environment Setup

```bash
python -m venv environment
.\environment\Scripts\activate         # On Windows
source environment/bin/activate       # On macOS/Linux
```

---

### 3. Install Dependencies

- Install Django:
  ```bash
  pip install Django
  django-admin --version
  ```

- Install project dependencies:
  ```bash
  pip install -r set1.txt
  ```

- Install necessary ML/DL libraries:
  ```bash
  pip install scikit-learn pandas numpy matplotlib seaborn tensorflow keras
  ```

---

### 4. Django Project Setup

```bash
django-admin startproject AcademicPredictor
cd AcademicPredictor
django-admin startapp PredictorApp
python manage.py migrate
python manage.py runserver
```

---

## 🚀 Project Execution Steps

### Step 1: Launch the Application

- Double-click `run.bat` or run the following:
  ```bash
  python manage.py runserver
  ```
- Open in browser: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### Step 2: Use Application Features

#### 🏠 Home Page

- Provides navigation to all prediction modules.
- Displays project overview with modal popups for guidance.

#### 📈 CGPA Prediction

- Input semester-wise SGPA.
- Predicts final CGPA using trained ML/DL models.

#### 🎯 SGPA Prediction

- Choose current semester and enter subject marks.
- Model returns predicted SGPA.

#### 📊 Attendance Prediction

- Enter subject-wise total and present hours.
- System calculates overall attendance percentage.

#### 📚 Marks & Grade Prediction

- Select semester and input internal/assignment/lab marks.
- Predicts subject-wise marks and letter grades.

#### 📋 Summary Reports

- Shows all previously entered and predicted results.
- Allows for cross-verification and download.

---

## 👨‍💻 Developed By - Nadeem Avulapalli



