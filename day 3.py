from typing import Any

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

total_wages = sum(employee[2] for employee in employees)
average_wages = total_wages / len(employees)
above_average = [employee[0] for employee in employees if employee[2] > average_wages]
print (f"Average wage is {average_wages:.2f}")

for employee in employees:
    if employee[2] > average_wages:
        print(f"{employee[0]} is above average wage")

