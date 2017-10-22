#Developed with Python 2.7
import string 

def convert_to_base(number, base):
    #Need uppercase chars for bases > 36, string.letters includes lower and upper cases
    ALL_CHARS = list(string.digits + string.letters)
    mods = []

    while number > 0:
        #Check to make sure the modulo result is not bigger than list lengeth.
        #If it is, just return something that is not a palindrome so the next base can be triggered.
        if number % base >= len(ALL_CHARS):
            return "next"

        mods.append(ALL_CHARS[number % base])
        number /= base

    return ''.join(mods[::-1])

def find_smallest_palindromic_base(number):
    current_base = 2

    while True:
        new_number = convert_to_base(number, current_base)
        
        if new_number == new_number[::-1]:
            return "{}, {}".format(number, current_base)

        current_base += 1

if __name__ == '__main__':
    for i in range(1, 1001):
        print find_smallest_palindromic_base(i)