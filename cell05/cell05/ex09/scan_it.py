#!/usr/bin/env python3
import re
import sys 
def main():
    lst = sys.argv
    if len(lst) == 1:# no parameter
        print("none")
    elif len(lst) > 3: # more that 2 parameter
        print("Error, must have 2 parameter")
    else:
        result = re.findall(lst[1], lst[2])
        print(len(result))

main()