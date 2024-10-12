amount_deposited=int(input('enter the amount: '))
if amount_deposited <=500000:
  IR=0.07*amount_deposited
else :
    IR=0.10*amount_deposited
first_year=IR+amount_deposited
print('amount_deposited_after_one_year: ',first_year)
second_year=first_year*0.7+amount_deposited
print('amount_deposited_after_two_years: ',second_year)
third_year=second_year*0.7+amount_deposited
print('amount_deposited_after_three_years: ',third_year)
