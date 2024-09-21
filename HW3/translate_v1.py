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

def num_translate(num_name):
    num_name = num_name.lower()
    if num_name in num_eng_rus:
        print(num_eng_rus.get(num_name))
    else:
        print(None)

while True:
    word_num = input()
    if word_num == 'stop' or word_num == 'Stop':
        break
    else:
        num_translate(word_num)
