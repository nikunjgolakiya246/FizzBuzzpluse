print("""
______   _              ______                                     
|  ___| (_)             | ___ \                        _       _   
| |_     _   ____  ____ | |_/ /  _   _   ____  ____  _| |_   _| |_ 
|  _|   | | |_  / |_  / | ___ \ | | | | |_  / |_  / |_   _| |_   _|
| |     | |  / /   / /  | |_/ / | |_| |  / /   / /    |_|     |_|  
\_|     |_| /___| /___| \____/   \____| /___| /___|
""")

def get_user_input(word):
    got_integer = False
    while not got_integer:
        try:
            value = int(input(f"Enter integer value for {word}: "))
            got_integer = True
        except Exception as e:
            print("Please make sure to enter integer value!")
    return value

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
    # Input values
    f = get_user_input("f")
    b = get_user_input("b")
    t = get_user_input("t")

    fizz_buzz_plus_plus(f,b,t)

    while True:
        response = input("Do You Want To Repeat? (yes/no)").lower()
        if response in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter yes/on")

    if response != "yes":
        break

input("Press enter to exit")
