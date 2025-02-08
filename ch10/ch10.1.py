
print("abc")

a = 3

b = 6
print(a, b)


# while True:
#     reply = input('Enter text:')
#     if reply == 'stop': 
#         break
#     elif reply.isdigit():
#         print(int(reply) ** 2)
#     else:
#         print(reply.upper())

# print('bye!')


while True:
    reply = input('Enter text:')
    if reply == 'stop': 
        break
    try:
        num = int(reply)
        print(num**2)
    except:
        print('Bad!' * 8)
            
print('Bye')


