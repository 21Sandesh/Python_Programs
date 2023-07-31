def word_list():
    with open("5_letter_words.txt", "r") as test:
        w = []
        for a in test:
            a.strip()
            w.append(a[:5])
        return w


def random_word(l):
    import random

    return random.choice(l)


def is_real_word(word1, l):
    return word1 in l


def check_guess(word1, w):
    testword = []
    for a in w:
        testword.append(a)
    c = ""
    for a in range(5):
        if word1[a] == w[a]:
            c += "X"
            testword.remove(word1[a])
        elif word1[a] in testword:
            c += "O"
            testword.remove(word1[a])
        else:
            c += "_"
    return c


def next_guess(testword):
    while True:
        word1 = input("Please enter a guess:")
        word1 = word1.lower()
        if is_real_word(word1, testword):
            break
        print("That's not a real word!")
    return word1


def play():
    testword = word_list()
    w = random_word(testword)
    a = 0
    print(w)
    while a < 6:
        word1 = next_guess(testword)
        a += 1
        print(check_guess(word1, w))
        if word1 == w:
            print("You won!")
            break
    else:
        print("you lost")


play()
