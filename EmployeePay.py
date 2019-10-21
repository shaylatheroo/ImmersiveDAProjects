# Using a text editor, write a program that calculates the salary for the week of the employees listed below.
# If an employee worked more than 40 hours that week, then calculate the remaining hours as time and a half (1.5x the normal rate).
# The program should print their name and salary earned.
#
# Do not use any libraries!

ID_Number = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010']
Emp_Name = ['Mary', 'John', 'Bob', 'Mel', 'Jen', 'Sue', 'Ken', 'Dave', 'Beth', 'Ray']
Pay_Rate = [15.00, 22.00, 35.00, 43.00, 17.00, 29.00, 40.00, 20.00, 37.00, 16.50]
Hours_Worked = [40, 25, 4, 62, 33, 45, 36, 17, 37, 80]

tracker = 0
Weekly_Pay = []

while tracker < len(ID_Number):
    emp_hours = Hours_Worked[tracker]
    emp_pay = Pay_Rate[tracker]
    if emp_hours > 40:
        total_pay = (40 * emp_pay) + ((emp_hours-40) * 1.5 * emp_pay)
    else:
        total_pay = emp_hours * emp_pay
    Weekly_Pay.append(total_pay)
    tracker += 1
    
print_tracker = 0
while print_tracker < len(ID_Number):
    print("Employee: " + Emp_Name[print_tracker] + "; Salary: $" + str("{:.2f}".format(Weekly_Pay[print_tracker])))
    print_tracker += 1
