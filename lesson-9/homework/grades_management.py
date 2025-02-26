import csv
from collections import defaultdict

grades_file = "grades.csv"
subject_grades = defaultdict(list)

with open(grades_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        subject = row["Subject"]
        grade = int(row["Grade"])
        subject_grades[subject].append(grade)

average_grades = {subject: sum(grades) / len(grades) for subject, grades in subject_grades.items()}

output_file = "average_grades.csv"

with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in average_grades.items():
        writer.writerow([subject, round(avg, 2)])

print(f"Average grades successfully written to {output_file}.")