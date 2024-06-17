# NASR TECH ARDHI UNIVERSITY
# BSc. Computer System AND  network
# 2024


def sum_even_numbers(my_list):
    even_sum = 0
    for num in my_list:
        if num % 2 == 0:
            even_sum += num
    print("the sum for all even numbers in the list is: " , even_sum)


if __name__== '__main__':
    my_list = [1,2,3,4,5,6,7,8,9]
    sum_even_numbers(my_list)  