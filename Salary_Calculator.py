basic_salary=int(input('Enter basic salary: '))
medical_Allowance=basic_salary*0.1
print('Medical Allowance: ',medical_Allowance)
conveyance_allowance=basic_salary*0.15
print(' Conveyance_Allowance: ',conveyance_allowance)     
house_rent=basic_salary*0.45
print( 'House_Rent: ',house_rent)     
gross_salary=basic_salary+medical_Allowance+conveyance_allowance+house_rent
print('Gross Salary is: ',gross_salary)
annual_gross_salary=gross_salary*12
print('Annual Gross Salary is: ',annual_gross_salary)
if  annual_gross_salary <= 200000:  
    tax = 0
elif annual_gross_salary >200000 or annual_gross_salary <=400000: 
       tax = (annual_gross_salary-200000)*0.1
elif annual_gross_salary >400000 or annual_gross_salary <=600000:
       tax=(annual_gross_salary-400000)*0.15+12500
elif annual_gross_salary >600000 or annual_gross_salary <=800000:
       tax=(annual_gross_salary-600000)*0.2+37500
else:
    tax = (income - 1500000) * 0.25 + 75000  
print('you owe the tax: ',tax)
net_salary=gross_salary-tax
print('Net Salary: ',net_salary)

                
