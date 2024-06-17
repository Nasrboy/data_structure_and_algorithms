
# NASR TECH ARDHI UNIVERSITY
# BSc. Computer System AND  network
# 2024


def print_right_triangle(height):
    for i in range(0 , height+1):
        for j in range(i):
            print("*", end=" ")
        print()

if __name__=="__main__": 
    print_right_triangle(5)        
