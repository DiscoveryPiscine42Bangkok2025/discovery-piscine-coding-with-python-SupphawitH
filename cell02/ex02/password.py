#!/usr/bin/env python3
def main():
    password = "Python is awesome"
    check = str(input("Enter password: "))
    if check == password:
        print("ACCESS GRANTED.")
    else:
        print("ACCESS DENIED.")
        
main()