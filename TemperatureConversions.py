#Matthew Muller
#TemperatureConversions
#CS-175L


def main():
    controlLoop()

def convertToKelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

def convertToCentigrade(fahrenheit):
    centigrade = (fahrenheit - 32) * 5/9
    return centigrade

def doConversion():
    fahrenheit = getFahrenheit()
    kelvin = convertToKelvin(fahrenheit)
    centigrade = convertToCentigrade(fahrenheit)
    print(f"Fahrenheit: {fahrenheit} Kelvin: {kelvin} Centigrade: {centigrade}")

def repeat():
    num_conversions = int(input('How many conversions do you want to do? '))
    for i in range(num_conversions):
        doConversion()

def controlLoop():
    while True:
        answer = input('Do you want to do the conversions (Yes or No)? ')
        if answer == 'Yes':
            repeat()
        elif answer == 'No':
            print('Goodbye!')
            break
    else:
        print('Invalid input. Enter Yes or No')

def getFahrenheit():
    while True:
        fahrenheit_input = input('Enter Fahrenheit temperature (must be -50 to 130): ')
        fahrenheit = int(fahrenheit_input)
        if -50 <= fahrenheit <= 130:
            return fahrenheit
        else:
            print('Invalid input. Please enter a valid temperature between -50 and 130')

def main():
    controlLoop()
if __name__ == '__main__':
    main()
