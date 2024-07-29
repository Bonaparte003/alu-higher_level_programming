#!/usr/bin/python3


def text_indentation(text):
    '''
    splits text basing on "?",":","."
    '''
    flag = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    non_space = text.strip()
    length = len(non_space)
    for i in range(length):
        if non_space[i] in ".?:":
            print(non_space[i])
            print()
            flag = 1
        else:
            if flag == 1 and non_space[i] == " ":
                continue
            print(non_space[i], end="")
            flag = 0
