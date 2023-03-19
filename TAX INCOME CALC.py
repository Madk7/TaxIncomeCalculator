#Program calculates income tax

#Given info:
#Flat tax rate of 20% (convert to decimal)
#$10,000 standard deduction (minus)
#Dependents = $3,000 deduction (multiply number then subtract)
#Gross income to 2 decimal point
#Income tax = decimal number

#Start with customer request phase:
#gross income, number of dependents
gross_income = float(input(("Enter the gross income (round to the nearest penny): ")))
number_dependent = int(input("Enter the number of dependents: "))

TAXRATE = 0.20
STANDARDDEDUCTION = 10000
DEPENDENTDEDUCTION = 3000


INCOMETAX = (gross_income - STANDARDDEDUCTION - (number_dependent*DEPENDENTDEDUCTION)) * TAXRATE
print("The income tax is $", INCOMETAX, sep = "")
