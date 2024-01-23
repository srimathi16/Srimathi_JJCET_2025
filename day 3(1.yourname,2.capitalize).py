#code1
#You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
#Hello firstname lastname! You just delved into python
#code
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

#code2
#You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
#Given a full name, your task is to capitalize the name appropriately    
    
    def solve(s):
    ans = s.split(' ')
    ans1 = (((i.capitalize() for i in ans)))
    return ' '.join(ans1)