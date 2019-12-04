import string as s
import random as r

passwordLength = r.randint(8,r.randint(9,30))
password = ''


for i in range(passwordLength):
    selector = r.randint(1,3)
    if selector==1:
        character = s.ascii_lowercase[r.randint(0,25)]
    elif selector==2:
        character = s.ascii_uppercase[r.randint(0,25)]
    else:
        character = s.digits[r.randint(0,9)]
    
    password += character


print(password)