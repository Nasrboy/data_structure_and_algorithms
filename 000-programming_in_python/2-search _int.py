

# NASR TECH ARDHI UNIVERSITY
# BSc. Computer System AND  network
# 2024

def find_first_occurrence(my_list, num):
    if num in my_list:
        give_index = my_list.index(num)
        print("The Index Of {} In Its First Occurrence Is : ".format(num),give_index)

#test the function
if __name__ == "__main__":
    my_list = [1,2,3,4,5,6,7,8,8,8,8,9,9,9]        
    find_first_occurrence(my_list,8)    