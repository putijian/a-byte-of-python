number = 23
running = True
while running:
    guess = int(input('你猜的数字：'))
    if guess == number:
        print('你猜对了')
        running = False
    elif guess < number:
        print('你采的数字小了')
    else:
        print('你猜的数字大了')
esle:print('竞猜截至')
