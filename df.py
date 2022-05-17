def computepay(hrs, rate):
  try:
    hrs = float(hrs)
    rate = float(rate)

    if hrs <= 40:
        pay = hrs * rate
    else:
        pay = 40 * rate + (hrs - 40) * rate * 1.5
    y = 'you have earned: $' + str(pay) 
    return print(y)                            
  except:
    print('Error, please enter numeric input')