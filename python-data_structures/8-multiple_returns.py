#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        sentence = 'None'
    return (len(sentence), sentence[0])
