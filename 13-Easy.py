# Primality Check
def isPrime(number):
    counter = 0
    maxTry = int(number / 2)

    for i in range(2, maxTry + 1):
        if number % i == 0:
            counter = counter + 1

    if counter == 0:
        return print(number,"is a prime numer!")
    else:
        return print(number, "is not a prime number!")


number = int(input("Enter a number: "))
isPrime(number)
