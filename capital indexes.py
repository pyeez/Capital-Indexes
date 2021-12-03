#import tkinter as tk

#window = tk.Tk()

#window.mainloop()

'''def capital_indexes(x = input("Enter a word: ")):
    m = []
    for i in x:
        if i.isupper():
            m.append(x.index(i))
    print(m)
    return

capital_indexes()'''

def capital_indexes(x = input("Enter a word: ")):
    a = []
    for index, letter in enumerate(x):
        if letter.isupper():
            a.append(index)

    print(a)
capital_indexes()

'''from string import uppercase
def capital_indexes(s):
    return [i for i in range(len(s)) if s[i] in uppercase]'''
