#!/usr/bin/env python3
import sys 
def main():
    lst = sys.argv
    if len(lst)-1 != 0:
        print(f"parameters: {len(lst)-1}")
        for i in lst[1:]:
            print(f"{i}: {len(i)}") 
    else:
        print("none")

main()