# Study of Python Fundamentals

This program is developed as part of the **study of Python fundamentals**, focusing on the use of **tuples, dictionaries, functions, and looping constructs**.

---

## Problem Description

A department wants to analyze the **academic performance of students** enrolled in a course in order to identify students who may require **academic support**.

Each student record contains:
- Student ID (String)
- Assignment score
- Internal test score
- Attendance percentage
- Hours studied per week

The system processes this data and generates a **structured performance report** for each student.

---

## Objectives of the Program

The Python program performs the following tasks:

1. Store all **student IDs in a tuple**.
2. Store student academic details using a **dictionary**.
3. Write a **function** to calculate the average score of a student.
4. Write a **function** to determine the academic risk level of a student.
5. Use **looping constructs** to process multiple student records.
6. Display a **structured performance report** for each student.

---

## Data Structures Used

Tuple (Student IDs)
```python
student_ids = ('S101', 'S102', 'S103', 'S104')
```
Dictionary (Student Details)
```python
students = {
    'S101': {'name': 'Asha', 'assignment': 78, 'test': 80, 'attendance': 92, 'hours': 8},
    'S102': {'name': 'Ravi', 'assignment': 65, 'test': 68, 'attendance': 85, 'hours': 5},
    'S103': {'name': 'Meena', 'assignment': 88, 'test': 90, 'attendance': 96, 'hours': 10},
    'S104': {'name': 'Kiran', 'assignment': 55, 'test': 58, 'attendance': 78, 'hours': 4}
}
```

---

## Functional Description

1. Average Score Calculation:
    - Calculates the mean of assignment and internal test scores.
2. Risk Level Determination
    - Students are categorized into:
        - Low Risk
        - Moderate Risk
        - High Risk based on average score, attendance percentage, and study hours.
3. Loop Processing
    - Iterates through multiple student records to generate reports.

---

## Output Description

For each student, the program displays:
- Student ID and Name
- Assignment and Test Scores
- Average Score
- Attendance Percentage
- Study Hours per Week
- Academic Risk Level
- Academic support requirement (if applicable)

---

## Concepts Covered

- Tuples
- Dictionaries
- Functions
- Conditional statements
- Looping constructs
- Structured output formatting

---

## Conclusion

This program demonstrates the practical application of Python fundamentals to analyze student performance data and identify students who may require academic support.