import re
from collections import defaultdict
from datetime import datetime

# -----------------------------
# Constants and Regex Patterns
# -----------------------------
VALID_ACTIVITIES = {"LOGIN", "LOGOUT", "SUBMIT_ASSIGNMENT"}
STUDENT_ID_PATTERN = re.compile(r"^S\d+$")
DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")
TIME_PATTERN = re.compile(r"\d{2}:\d{2}")

# -----------------------------
# Student Class
# -----------------------------
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.activities = []

    def add_activity(self, activity, date, time):
        self.activities.append((activity, date, time))

    def activity_summary(self):
        summary = defaultdict(int)
        for activity, _, _ in self.activities:
            summary[activity] += 1
        return summary


# -----------------------------
# Generator to Read Log File
# -----------------------------
def read_log_file(filename):
    """Generator that yields one valid log entry at a time"""
    with open(filename, "r") as file:
        for line_no, line in enumerate(file, start=1):
            try:
                parts = [p.strip() for p in line.split("|")]
                if len(parts) != 5:
                    raise ValueError("Invalid format")

                student_id, name, activity, date, time = parts

                if not STUDENT_ID_PATTERN.match(student_id):
                    raise ValueError("Invalid Student ID")

                if activity not in VALID_ACTIVITIES:
                    raise ValueError("Invalid activity type")

                if not DATE_PATTERN.match(date) or not TIME_PATTERN.match(time):
                    raise ValueError("Invalid date or time")

                yield student_id, name, activity, date, time

            except Exception as e:
                print(f"[ERROR] Line {line_no}: {e} -> {line.strip()}")


# -----------------------------
# Main Processing Function
# -----------------------------
def process_logs(input_file, output_file):
    students = {}
    daily_stats = defaultdict(lambda: defaultdict(int))
    abnormal_behavior = defaultdict(list)

    for student_id, name, activity, date, time in read_log_file(input_file):

        if student_id not in students:
            students[student_id] = Student(student_id, name)

        students[student_id].add_activity(activity, date, time)
        daily_stats[date][activity] += 1

    # Detect abnormal behavior (multiple logins without logout)
    for student in students.values():
        login_count = 0
        for activity, _, _ in student.activities:
            if activity == "LOGIN":
                login_count += 1
            elif activity == "LOGOUT":
                login_count -= 1

            if login_count > 1:
                abnormal_behavior[student.student_id].append("Multiple logins without logout")

    # -----------------------------
    # Generate Report
    # -----------------------------
    with open(output_file, "w") as f:
        print("\n===== STUDENT ACTIVITY REPORT =====")
        f.write("===== STUDENT ACTIVITY REPORT =====\n")

        for student in students.values():
            summary = student.activity_summary()
            report = (
                f"\nStudent ID: {student.student_id}\n"
                f"Name: {student.name}\n"
                f"Total Logins: {summary.get('LOGIN', 0)}\n"
                f"Total Submissions: {summary.get('SUBMIT_ASSIGNMENT', 0)}\n"
            )

            print(report)
            f.write(report)

        print("\n===== DAILY ACTIVITY STATISTICS =====")
        f.write("\n===== DAILY ACTIVITY STATISTICS =====\n")

        for date, stats in daily_stats.items():
            line = f"{date} -> {dict(stats)}"
            print(line)
            f.write(line + "\n")

        print("\n===== ABNORMAL BEHAVIOR =====")
        f.write("\n===== ABNORMAL BEHAVIOR =====\n")

        if abnormal_behavior:
            for sid, issues in abnormal_behavior.items():
                line = f"{sid}: {issues}"
                print(line)
                f.write(line + "\n")
        else:
            print("No abnormal behavior detected")
            f.write("No abnormal behavior detected\n")


# -----------------------------
# Program Entry Point
# -----------------------------
if __name__ == "__main__":
    INPUT_FILE = "student_log.txt"
    OUTPUT_FILE = "activity_report.txt"
    process_logs(INPUT_FILE, OUTPUT_FILE)
