list_of_cube = []

for i in range(1000):
    if i%2 != 0:
        num = i ** 3
        list_of_cube.append(num)
        print(i, num)
    else:
        continue

def s_n(num):
    s = 0
    while num:
        s += num % 10
        num //= 10
    return s

for j in list_of_cube:
    s_num = s_n(j)
    if s_num%7 == 0:
        print(j, s_num)

for z in list_of_cube:
    s_num = s_n(z + 17)
    if s_num%7 == 0:
        print(z, s_num)
