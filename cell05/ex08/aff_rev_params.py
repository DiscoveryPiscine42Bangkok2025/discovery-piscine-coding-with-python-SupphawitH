#!/usr/bin/env python3
import sys 
def main():
    lst = sys.argv
    if len(lst) <= 2: # 1: script name, 2: 1st agrv
        print("none")
    else: 
        for i in reversed(lst[1: ]):
            print(i)

main()
