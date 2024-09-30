# Variables
hrs = None
rte = None

# Function that determines overtime and computes total weekly pay
def computepay(hours, rate):
    if hours > 40:
        pay = (rate * 40) + ((hours - 40) * (rate * 1.5))
    else:
        pay = (rate * hours)
    return pay


# Receive input for hrs variable, loops until the number is a valid float greater than zero
while True:
    print('please input how many hours you work per week.')
    hrs = input('hours: ')
    try:
        hrs = float(hrs)
        if hrs > 0:
            break
        else:
            print('please input a number greater than zero.')
            print('-----------------------------')
    except:
        print('ERROR', hrs, 'is not a valid number')
        print('-----------------------------')

# Receive input for rte variable, loops until the number is a valid float greater than zero
while True:
    print('please input your hourly rate.')
    rte = input('rate: ')
    try:
        rte = float(rte)
        if rte > 0:
            break
        else:
            print('please input a number greater than zero.')
            print('-----------------------------')
    except:
        print('ERROR', rte, 'is not a valid number')
        print('-----------------------------')

pay = str(computepay(hrs, rte))

print(f'your weekly pay is ', pay)
