import random
import string

#Kneepads2 - Dylan - 5/17/2021

print("\nPassword Generator\n============================\n")

passwordSize = int(input("Enter the desired length of your password: "))

#could ask for input for how complex the user wants their password
#maybe like 'Enter 1 for just lowercase letters, 2 for just uppercase letters, 3 for just digits, 4 for 1 and 2, 5 for all' or something 

def id_generator(size = passwordSize, chars = string.ascii_uppercase + string.digits + string.ascii_lowercase): 
    print (''.join(random.choice(chars) for _ in range(size)))

    #string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #string.digits = '0123456789'
    #string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

id_generator()