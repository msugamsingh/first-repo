#! /usr/bin/python3

def chop_ascending(any_str):
    for i in range(-1, -len(any_str), -1):
        print(any_str[0:-i])
    print(any_str)
# [0:-2] == [:-2] ==> from start to second last.

def chop_decending(any_str):
    print(any_str)
    for i in range(-1, -len(any_str), -1):
        print(any_str[:i])
# for more info add 'print(i)' into the loop.

'''TESTING'''

string = 'shobhit'
chop_ascending(string)
print('\n')
chop_decending(string)
