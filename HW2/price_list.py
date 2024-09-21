import random

price_list = []
i = 0
while i < 20:
    price_list.append(round(random.uniform(01.00, 100.00), 2))
    i += 1

print(price_list)

price_list.sort()

print(price_list)

price_list_less = sorted(price_list, reverse=True)

print(price_list_less)

for i in price_list:
    num_r = int(i//1)
    num_k = int(((i)*100)%100)
    print('{0:02d} руб {1:02d} коп'.format(num_r, num_k))

print('-----')

i = 0
while i <= 4:
    num_r = int(price_list_less[i]//1)
    num_k = int(((price_list_less[i])*100)%100)
    print('{0:02d} руб {1:02d} коп'.format(num_r, num_k))
    i += 1