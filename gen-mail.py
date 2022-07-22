import random
import string

num = 100 #Value amount email
length = 10 # length string 

for i in range(num):
    # get random string of length without repeating letters
    result_str = ''.join(random.sample(string.ascii_lowercase + string.digits, length))
    print("Gmail :",result_str+"@mail.com")

    # gen password
    password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
    print("password :", password)

    #read and write seve in file
    txt = open('example.txt','a')

    txt.write(result_str + '@mail.com\n')
    txt.write(password+'\n')
    txt.close()