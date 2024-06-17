# NASR TECH ARDHI UNIVERSITY
# BSc. Computer System AND  network
# 2024

import math
def is_prime(number):
    if number < 2:
        return False
    for i in range(2,int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True
if __name__ == "__main__":
    print(is_prime(25))  # Should return False
    print(is_prime(5))  # Should return True
   
    