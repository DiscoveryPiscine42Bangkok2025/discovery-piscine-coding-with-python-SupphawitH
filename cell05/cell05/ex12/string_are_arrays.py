#!/usr/bin/env python3
import sys 
import re
def main():
    lst = sys.argv
    if len(lst) == 2:
        result = re.findall('z', lst[1])
        if len(result) != 0:
            print("z"*len(result))
        else:
            print("none")
    else:
        print("none")

main()