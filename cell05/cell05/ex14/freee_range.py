#!/usr/bin/env python3
import sys 
def main():
    lst = sys.argv
    if len(lst) == 3:
        idx1 = int(lst[1])
        idx2 = int(lst[2])
        output = [i for i in range(idx1, idx2+1)]
        print(output)
    else:
        print("none")
       
main()