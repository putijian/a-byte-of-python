while True:
    s = input('Enter something:');#这个是对S 进行赋值，赋值你是输入的
    if s == 'quit': #如果输入的相同，那么就退出
        break
    print('Length of the string is', len(s))#否则计算出字符的长度
    print('done')#输入计算完成