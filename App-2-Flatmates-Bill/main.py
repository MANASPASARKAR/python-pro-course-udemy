from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Enter Total Bill: "))
period = str(input("Enter Period: "))

name1 = str(input("Enter name of flatmate 1: "))
name1_days = int(input(f"Enter the days {name1} were in the House during the billing period: "))

name2 = str(input("Enter name of flatmate 2: "))
name2_days = int(input(f"Enter the days {name2} were in the House during the billing period: "))

f1 = Flatmate(name = name1, days_in_house = name1_days)
f2 = Flatmate(name = name2, days_in_house = name2_days)
bill = Bill(amount, period)

print(f"{f1.name} Pays: ", f1.pays(bill=bill, flatmate2=f2))
print(f"{f2.name} Pays: ", f2.pays(bill=bill, flatmate2=f1))
pdf_report = PdfReport(filename=f"{bill.period} Report.pdf")
pdf_report.generate(flatmate1=f1, flatmate2=f2, bill=bill)