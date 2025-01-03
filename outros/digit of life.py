def digit_of_life(num):
    num = str(num)

    result = 0
    start = False

    while result >= 10 or start == False:
        result = 0
        for n in num:
            result += int(n)
        num = str(result)      
        start = True

    print(result)

digit_of_life(20000101)