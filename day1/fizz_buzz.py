def fizz_buzz(number):
    '''
    this a fizz_buzz that prints the number if it is not divisible by 3 or 5
    prints buzz if the number is divisible by 5 only
    prints fizz if the number is divible by 3 only
    prints FizzBuzz if the number is divible by both 3 and 5 '''

    number3 = "Fizz"
    number5 = "Buzz"    
   
    if number % 3 == 0 and number % 5 == 0:
        allnumber = number3, number5
        value = "".join(allnumber)
            
    elif number % 5 == 0:
        value = number3
        
    elif number % 3 == 0:
        value = number5

    else:
        value  = number
    return value
        
print(fizz_buzz(7))    
