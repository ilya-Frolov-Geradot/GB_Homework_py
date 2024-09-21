l_f_c = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while True:
    if i >= len(l_f_c):
        break
    try:
        num = int(l_f_c[i])
        ind = l_f_c.index(l_f_c[i])
        num_fc = list(l_f_c[i])
        if num_fc[0] in ('+' or '-'):
            l_f_c[i] = l_f_c[i].zfill(len(num_fc)+1)
        else:
            l_f_c[i] = l_f_c[i].zfill(2)
        l_f_c.insert(ind, '"')
        l_f_c.insert(ind+2, '"')
        i += 2
    finally:
        i+= 1
        continue

f_pri = " ".join(l_f_c)
print(f_pri)

