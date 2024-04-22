def generatePattern(type, size):
    if type == 1:
        for i in range(0, size):
            for j in range(0, 2* (size-i)-1):
                print(" ", end="")
            for k in range(0, 2 * i + 1):
                print("*", end=" ")
            print("\n")

    elif type == 2:
        for i in range(0, size):
            for j in range(0, size):
                print("*", end="   ")
            print("\n")
    
    elif type == 3:
        for i in range(0, size):
            for j in range(0, size-i-1):
                print(" ", end="")
            for k in range(0, size):
                print("*", end="   ")
            print("\n")

while(1):
    print("Enter the type of pattern to make:\n1. Triangle\n2. Square\n3. Rhombus\n0. Exit\n")
    typePattern = int(input())
    print("Enter the Height of the pattern: ")
    height = int(input())
    print("\n")
    if typePattern == 0:
        break
    generatePattern(typePattern, height)

    