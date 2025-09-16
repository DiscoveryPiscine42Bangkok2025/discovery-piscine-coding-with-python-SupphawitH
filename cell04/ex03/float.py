#!/usr/bin/env python3
def main():
    num = float(input("Give me a number: "))
    if num == round(num):
        print("This number is an integer.")
    else:
        print("This number is a decimal")

main()
    