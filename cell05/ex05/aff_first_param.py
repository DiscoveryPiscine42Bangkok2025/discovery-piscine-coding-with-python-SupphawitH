#!/usr/bin/env python3
import sys 
def main():
    #run on powershell with wsl
    lst = sys.argv
    if len(lst) > 1:
        print(lst[1]) #index 0 == script name
    else:
        print("none")
        
main()