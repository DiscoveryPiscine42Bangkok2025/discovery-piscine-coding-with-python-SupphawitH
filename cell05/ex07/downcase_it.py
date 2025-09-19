#!/usr/bin/env python3
import sys 
def main():
    #run on powershell with wsl
    lst = sys.argv
    if len(lst) != 2:
        print("none")
    else:
        output = str(lst[1]).lower() #index 0 == script name
        print(output)


main()