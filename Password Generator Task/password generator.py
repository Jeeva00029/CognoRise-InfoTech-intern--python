"""
***************Password Generator*********************
To get user input need weak password or strong password
   (i) Weak Password
        --to display randomly anyone of listed weak password
   (2) Strong Password
        --To get user input (length of password)
        --To get user input how many letters to need
        --To get user input how many digits to need
        --To get user input how many punctuation to need
        -- After to generate a strong password
"""
import random
print("*****************************************")
print("*       --PASSWORD GENERATOR--          *")
print("*****************************************")
print()
weak_password=["12345","11111","Admin","password","00000","1234567890","qwerty","55555","admin123","abc123",
               "iloveyou","money","Welcome","!@#$%^&*","ronaldo","prince","jesus","abcdefgh","rose","freedom",
               "strength","password123","Master","12341234","656565","25252525","Computer","123123123","Google123",
               "yourname123"]
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x'
         ,'y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
         'W','X','Y','Z']
digits=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','$','#','%','^','&','*','(',')','-','_','+','/','[',']','{','}','|',';',':','.','>','<'
         ,'?','~']
pass_type=input("Password Type (Weak/Strong):").lower()
if(pass_type=="weak"):
    password=random.choice(weak_password)
    print("Password:",password)
elif(pass_type=="strong"):
    let=int(input("Enter how many letters you need:"))
    dig=int(input("Enter how many digits you need:"))
    sym=int(input("Enter how many symbols you need:"))
    password_list=[]
    for i in range(1,let+1):
        seq=random.choice(letters)
        password_list.append(seq)
    for i in range(1,dig+1):
        seq=random.choice(digits)
        password_list.append(seq)
    for i in range(1,sym+1):
        seq=random.choice(symbols)
        password_list.append(seq)
    random.shuffle(password_list)
    password="".join(password_list)
    print("Password:",password)
else:
    print("Give a right input (weak/strong)")
print("******THANK YOU*******")