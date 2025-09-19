#!/usr/bin/env python3
def main():
    '''play with arrays += 2'''
    lst = [2, 8, 9, 48, 8, 22, -12, 2]
    l1 = [i for i in lst if i>5] # greater that 5 
    st = set([i+2 for i in l1]) # + 2 all 
    print(lst)
    print(st)

main()