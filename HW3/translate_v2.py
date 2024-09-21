num_eng_rus = {
        'zero':'ноль',
        'one': 'один',
        'two':'два',
        'three':'три',
        'four':'четыре',
        'five':'пять',
        'six':'шесть',
        'seven':'семь',
        'eight':'восемь',
        'nine':'девять',
        'ten':'десять'
    }

def num_translate_adv(num_name):
    num_check = num_name.lower()
    if (num_check in num_eng_rus) and (num_name == num_check.capitalize()):
        name_for_print = num_eng_rus.get(num_check).capitalize()
        print(name_for_print)
    elif num_check in num_eng_rus:
        name_for_print = num_eng_rus.get(num_check)
        print(name_for_print)
    else:
        print(None)

while True:
    word_num = input()
    if word_num == 'stop' or word_num == 'Stop':
        break
    else:
        num_translate_adv(word_num)