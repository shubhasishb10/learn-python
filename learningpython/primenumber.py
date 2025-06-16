import stringpractice

def is_prime_number(num):
    if num%2==0:
        print("Num ", num, " is prime number")
    else:
        print("Num ", num, " is not a prime number")

stringpractice.print_star(20, stringpractice.Align.RIGHT)


is_prime_number(13)