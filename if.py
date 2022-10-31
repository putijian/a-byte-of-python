number = 23
guess = int(input('你猜的数字:'))
if guess == number:
    print('你猜对了')
elif guess < number:
    print('数字小了')
else:
    print('数字大了')
print('DONE')