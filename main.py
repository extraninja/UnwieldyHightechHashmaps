def computepay(hrs, rate):
  if hrs <= 40:
     pay = hrs * rate
  else:
     pay = 40 * rate + (hrs - 40) * rate * 1.5
  return pay
  
check = True
while(check == True):
  try:
    hrs = input('Enter hours: ')
    hrs = float(hrs)
    rate = input('Enter pay rate: ')
    rate = float(rate)
    
    pay = computepay(hrs, rate)
    y = 'According to computepay, you have earned: $'+ str(pay)
    print(y) 
    check = False
  except:
    print('Error, please enter numeric input \n')
    check = True
