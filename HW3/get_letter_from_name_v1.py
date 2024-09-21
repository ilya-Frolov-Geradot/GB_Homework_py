letter_dict = {}
name_list = ['Варвара','Юлия','дмитрий','Илья','Михаил','РуслаН','Роман','Владислав','Тимофей','семён','Ева','Савелий','Егор','Мия','Ульяна','Давид','Елизавета','Артём','Амина','Александра']
def letter_from_name (name_list):
    for i in range(len(name_list)):
        name_list[i] = name_list[i].capitalize()
    for j in name_list:
        if j[0] in letter_dict:
            letter_dict[j[0]].append(j)
        else:
            letter_dict[j[0]] = [j]


    for i in sorted(letter_dict.items()):
        print(i)

letter_from_name(name_list)


