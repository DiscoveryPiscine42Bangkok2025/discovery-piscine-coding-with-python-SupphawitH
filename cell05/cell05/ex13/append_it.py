#!/usr/bin/env python3
import sys 
import re
def main():
    lst = sys.argv
    if len(lst) == 1:
        print("none")
    else:
        for i in lst[1:]:
            if i.endswith("ism"):
                pass
            else:
                print(f"{i}ism")
        
main()