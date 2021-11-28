import os
print("1. shutdown your pc:")
print("2. restart your pc:")
print("3. exit")
choice = int(input('\n enter your choice:'))
if choice == 1:
    sec = int(input('enter number of seconds:'))
    strone = "shutdown /s /t "
    strtwo = str(sec)
    str = strone + strtwo
    os.system(str)
elif choice == 2:
    sec = int(input('enter number of seconds:'))
    strone = "shutdown /r /t "
    strtwo = str(sec)
    str = strone + strtwo
    os.system(str)
elif choice == 3:
        exit()
else:
        print('Wrong choice')

