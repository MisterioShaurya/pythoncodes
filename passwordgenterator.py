import random
import string
file1 = open("generatedpass.txt","a")
all_characters = string.ascii_letters+string.digits+string.punctuation
lenght = int(input("Enter the lenght of your password:"))
use = input("Enter the purpose:")
password = "".join(random.choices(all_characters,k=lenght))
file1.write(f"Your for password {use} is: {password} \n")
file1.close()
print(f"Your password is: {password}")