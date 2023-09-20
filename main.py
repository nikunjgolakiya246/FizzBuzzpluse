print("""
______   _              ______                                     
|  ___| (_)             | ___ \                        _       _   
| |_     _   ____  ____ | |_/ /  _   _   ____  ____  _| |_   _| |_ 
|  _|   | | |_  / |_  / | ___ \ | | | | |_  / |_  / |_   _| |_   _|
| |     | |  / /   / /  | |_/ / | |_| |  / /   / /    |_|     |_|  
\_|     |_| /___| /___| \____/   \____| /___| /___|
""")

def fizz_buzz_plus_plus(f, b, t):
    counter = 0
    prev_word = ""

    for num in range(1, t + 1):
        output = ""

        if num % f == 0:
            if prev_word == "Fizz":
                counter += 1
            else:
                counter = 0
            output = "Fizz" + "+" * (counter)
            prev_word = "Fizz"

        if num % b == 0:
            if prev_word == "Buzz":
                counter += 1
            else:
                counter = 0
            output = "Buzz" + "+" * (counter)
            prev_word = "Buzz"

        if num % f == 0 and num % b == 0:
            output = "FizzBuzz"
            counter = 0
            prev_word = ""

        if not output:
            output = str(num)

        print(output)

while True:

    try:
        # Input values
        f = int(input("Enter integer value for f: "))
        b = int(input("Enter integer value for b: "))
        t = int(input("Enter integer value for t: "))

        fizz_buzz_plus_plus(f,b,t)

    except ValueError:
        print("Invalid input. Please enter integer values for f, b, and t.")

    while True:
        response = input("Do You Want To Repeat? (yes/no)").lower()
        if response in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter yes/on")

    if response != "yes":
        break

input("Press enter to exit")
