def prime_checker(number):
    prime_number = True

    for i in range(2, number):
        if number % i == 0:
            prime_number = False

    if prime_number == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)


# ----------------------- Result 1 ----------------------- #
# Check this number: 22
# It's not a prime number.


# ----------------------- Result 2 ----------------------- #
# Check this number: 23
# It's a prime number.
