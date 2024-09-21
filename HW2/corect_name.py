l_n_c = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# for i in range(len(l_n_c)):
#     l_n_c[i] = l_n_c[i].split(' ')
#     l_n_c[i][0] = l_n_c[i][0].capitalize()
#     l_n_c[i][-1] = l_n_c[i][-1].capitalize()
#     if len(l_n_c[i])>2:
#         l_n_c[i][0] = ' '.join(l_n_c[i][:-1])
#         del l_n_c[i][1:-1]
#     l_n_c[i] = ', '.join(l_n_c[i])
#
# print(l_n_c)

for i in range(len(l_n_c)):
    l_n_c[i] = l_n_c[i].split(' ')[-1].capitalize()
    print(f'Привет, {l_n_c[i]}!')