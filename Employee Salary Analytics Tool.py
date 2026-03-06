import csv
from collections import defaultdict
from datetime import datetime
def load_data(filename):
    try:
        with open(filename, newline="") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Error : '{filename}' does not exist.")
        return[]

def process_data(data):
    department_total = defaultdict(int)
    department_count = defaultdict(int)
    above_8000_count =0
    above_30_count =0

    highest_salary = 0
    highest_paid_employee =None

    for row in data:
        name = row["name"]
        department = row["department"]
        salary = int(row["salary"])
        age = int(row["age"])

        department_total[department]+=salary
        department_count[department]+=1

        if salary > 8000:
            above_8000_count+=1
        
        if age >30:
            above_30_count+=1

        if salary > highest_salary:
            highest_salary = salary
            highest_paid_employee = name
    averages = {}
    for dept in department_total:
        averages[dept]=department_total[dept] / department_count[dept]
    return averages, above_8000_count, highest_paid_employee, highest_salary,above_30_count

def save_data(averages, above_8000_count, highest_paid_employee, highest_salary,above_30_count):
    date_str = datetime.today().strftime("%Y_%m_%d")
    filename = f"summary_{date_str}.csv"
    with open(filename ,"w",newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Departments","Average Salary"])
        for department in sorted(averages):
            writer.writerow([department,f"{averages[department]:.2f}"])
        writer.writerow([])
        writer.writerow(["Above_8000_count",above_8000_count])
        writer.writerow([])
        writer.writerow(["Above_30_count",above_30_count])
        writer.writerow([])
        writer.writerow(["Highest Paid employee","Salary"])
        writer.writerow([highest_paid_employee,highest_salary])
    return filename

def generate_summary(averages, above_8000_count, highest_paid_employee, highest_salary,above_30_count):
    print("-----")
    print("Average Salary by department: ")
    for department in sorted(averages):
        print(f"{department} : {averages[department]:.2f}")
    print(f"\nNumber of employess having Salary above 8000: {above_8000_count}")
    print(f"\nNumber of employess age greater than 30: {above_30_count}")
    print(f"\nHigest Paying employee: {highest_paid_employee} :{highest_salary}")
    print("-----")

def main():
    data= load_data("employees.csv")
    averages, above_8000_count, highest_paid_employee, highest_salary,above_30_count = process_data(data)
    generate_summary(averages, above_8000_count, highest_paid_employee, highest_salary,above_30_count)
    saved_file = save_data(averages, above_8000_count, highest_paid_employee, highest_salary,above_30_count)
    print(f"\nSummary saved to: {saved_file}")

if __name__ == "__main__":
    main()

