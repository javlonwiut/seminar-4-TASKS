def countdown(n):
    if n <= 0:
         print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)


def countup(n):
    if n >= 0:
        print("Blasstof")     
    else:
        print(n)
        countup(n+1)  


while True:    
    try:
        client_number = int(input("Write only number here: "))
        break
    except ValueError:
        print("It is not a number")


if client_number < 0:
    countup(client_number)
elif client_number > 0:
    countdown(client_number)
else:
    countdown(client_number)  
