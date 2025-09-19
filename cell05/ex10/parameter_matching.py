#!/usr/bin/env python3
import sys 
def main():
    lst = sys.argv
    check = str(input("What was the paremeter? "))
    if lst[1] == check:
        print("Good job!")
    else:
        print("Nope, sorry...")
main()