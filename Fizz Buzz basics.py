for number in range(1,101):
    fizz_buzz=" "
    if number % 15==0:
        fizz_buzz=fizz_buzz + "Fizz Buzz"
    elif number % 5==0:
        fizz_buzz=fizz_buzz + "Buzz"
    elif number % 3==0:
        fizz_buzz=fizz_buzz + "Fizz"
    else:
        fizz_buzz=fizz_buzz + str(number)
    print(fizz_buzz)
    
