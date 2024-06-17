
# NASR TECH ARDHI UNIVERSITY
# BSc. Computer System AND  network
# 2024

def character_frequency(string):
    frequency_dict = {} # for storing those answers of chars
    string = string.lower() # this convert into lowercase
    for char in string:
        if char.isalpha(): #check if is it real char if not escaped from itteration
            if char in frequency_dict:
                frequency_dict[char] += 1 # if char present it increment by one
            else:
                frequency_dict[char] = 1 # if not present record its frequence into dictionary
    return frequency_dict
# Test the function

if __name__ == '__main__':
    print(character_frequency("I am a student of ardhi university"))
            