import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def random_word_not_again(w_cheak, f_cheak, f_get):
    while True:
        if w_cheak in f_cheak:
            w_cheak = random.choice(f_get)
        else:
            break
    return w_cheak


def make_bad_joke(time):
    cheak = (input('Слова могут повторятся? Y/N: ')).lower()
    if cheak == 'n' and time <= 5:
        n = []
        ad = []
        aj = []
        for i in range(time):
            noun = random.choice(nouns)
            adv = random.choice(adverbs)
            adj = random.choice(adjectives)
            noun = random_word_not_again(noun, n, nouns)
            adv = random_word_not_again(adv, ad, adverbs)
            adj = random_word_not_again(adj, aj, adjectives)
            print("{0} {1} {2}".format(noun.capitalize(), adv, adj))
            n.append(noun)
            ad.append(adv)
            aj.append(adj)
    elif cheak == 'n' and time > 5:
        print('В этом случаи это не возможно')
    elif cheak == 'y':
        for i in range(time):
            noun = (random.choice(nouns)).capitalize()
            adv = random.choice(adverbs)
            adj = random.choice(adjectives)
            print("{0} {1} {2}".format(noun, adv, adj))

jk_count = int(input('Сколько вы хотите шуток: '))
make_bad_joke(jk_count)