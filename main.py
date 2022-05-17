#name=input('what\'s your name? ')
#print('Hello', name)

#inp=input('Europe floor number? ')
#usf=int(inp)+1
#print('USA floor number = ', usf)

#hrs = input('Enter hours: ')
#rate = input('Enter pay rate: ')
#if float(hrs) <= 40:
#  pay = float(hrs) * float(rate)
#else : 
#  pay = 40 * float(rate) + (float(hrs) - 40) * float(rate) * 1.5
#print('You have earned: ', pay)

print (99/100)

try:
    hrs = input('Enter hours: ')
    hrs = float(hrs)
    rate = input('Enter pay rate: ')
    rate = float(rate)

    if hrs <= 40:
        pay = hrs * rate
    else:
        pay = 40 * rate + (hrs - 40) * rate * 1.5
    y = 'you have earned: $' + str(pay)                             
    print(y)

except:
    print('Error, please enter numeric input')

