def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to √n
        if n % i == 0:
            return False  # If divisible by any number other than 1 and n, it is not prime
    return True  # If no divisors were found, it is prime

# Loop through numbers from 1 to 100
for number in range(1, 101):
    if is_prime(number):
        print(number)

