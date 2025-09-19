#!/usr/bin/env python3
import sys 
def main():
    lst = sys.argv
    if len(lst) != 2:
        print("none")
    else:
        check = str(input("What was the paremeter? "))
        if lst[1] == check:
            print("Good job!")
        else:
            print("Nope, sorry...")
main()