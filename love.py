print('\t\t\t\t\t welcome to love test meter:')
A = input('\n enter your BF first char of name:')
B = input('\n enter your GF first char of name:')
result = (ord(A)*ord(B))/100
if result <= 50:
    print('result = %0.2f'%result)
    print()('you are in fake love!')
    print('\U0001F614')
else:
    print('result = %0.2f'%result)
    print('you are in tru....... love!')
    print('\U0001F603')

x = input('press enter to exit')

