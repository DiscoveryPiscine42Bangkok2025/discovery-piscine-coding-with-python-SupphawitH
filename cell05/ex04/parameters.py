#!/usr/bin/env python3
import sys
def main():
    #run on powershell with wsl
    result = len(sys.argv) - 1
    print(f"Number of parameters: {result}")
    
main()
    