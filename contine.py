i = 0
while True:

    s = input('Enter something,')
    i = i + 1
    if s == 'quit':
        print('你猜了',i,'次')
        break
    if len(s)<5:
        print("字符太短")
        print('你猜了',i,'次')
        continue

    print('字符的长度',len(s))
    print('你猜了',i,'次')