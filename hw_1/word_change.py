i = 1
for i in range(101):
    if i%10 == 1 and (10 > i or i > 20):
        print(f'{i} процент')
    elif (i%10 == 2 or i%10 == 3 or i%10 == 4) and (10 > i or i > 20):
        print(f'{i} процента')
    else:
        print(f'{i} процентов')
