name=input('Enter your name=')
#PRINTING THE NAME
print('Your name is',name)
Celcius=float(input('Enter the temrature value in celcius'))
fahrenheit=(Celcius*1.8)+32
print('fahrenheit value is',fahrenheit )
if (fahrenheit>=104):
    print('Its to Hot')
elif (fahrenheit<=50):
    print('Its to cold')
else:
    print('the temprature is nice')