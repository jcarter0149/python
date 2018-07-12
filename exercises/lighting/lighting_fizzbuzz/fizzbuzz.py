for num in range(1, 100):
    if(num % 15 == 0):
        print("Fizz buzz")
    elif(num % 5 == 0):
        print("Buzz")
    elif(num % 3 == 0):
        print("Fizz")
    else:
        print(num)
