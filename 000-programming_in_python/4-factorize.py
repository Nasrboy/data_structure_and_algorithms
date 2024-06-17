# NASR TECH ARDHI UNIVERSITY
# BSc. Computer System AND  network
# 2024

def factorize(number):
    if number < 2:
        return []

    prime_factors = [] #store factors
    divisor = 2

    while number >= 2:
        while number % divisor == 0:
            prime_factors.append(divisor)
            number = number // divisor
        divisor += 1

    return prime_factors

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number to factorize: "))
    print("Prime factors:", factorize(number))

