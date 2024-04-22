import time

takeInput: float = 0
def getInput():
    takeInput = float(input("Enter the value: "))
    return takeInput


def cel2fah(val):
    result = (val * 9/5) + 32
    print("==> ", result, "°F\n")

def fah2cel(val):
    result = (val - 32) * 5/9
    print("==> ", result, "°C\n")

def cel2kelvin(val):
    result = val + 273.15
    print("==> ", result, "°K\n")

def kelvin2cel(val):
    result = val - 273.15
    print("==> ", result, "°C\n")

def kelvin2feh(val):
    result = (val - 273.15) * 9/5 + 32
    print("==> ", result, "°F\n")

def fah2kelvin(val):
    result = (val - 32) * 5/9 + 273.15
    print("==> ", result, "°K\n")


while(1):
    time.sleep(2)
    print("+++ Temperature Conversion System +++ \n\n")
    print("1. Celsius to Fahrenheit.")
    print("2. Fahrenheit to Celsius.")
    print("3. Celsius to Kelvin.")
    print("4. Kelvin to Celsius.")
    print("5. Fahrenheit to Kelvin.")
    print("6. Kelvin to Fahrenheit.")
    print("0. Exit\n")
    key = int(input("Enter Key to perform an action: "))
    
    if key == 1:
        value = getInput()
        cel2fah(value)
    
    elif key == 2:
        value = getInput()
        fah2cel(value)
    
    elif key == 3:
        value = getInput()
        cel2kelvin(value)
    
    elif key == 4:
        value = getInput()
        kelvin2cel(value)
    
    elif key == 5:
        value = getInput()
        fah2kelvin(value)
    
    elif key == 6:
        value = getInput()
        kelvin2feh(value)

    elif key == 0:
        break
    else:
        print("Wrong key pressed, Please try again!")

