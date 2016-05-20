#File:leapyear86448.py
#Author:Simmy Payyappilly Varghese,Student ID:86448
#Date Created:03/20/2015
"""This program determines if a year is leap year or not

   If a year is divisible by 400 it is a leap year also if a year divisible by 4 and not divisible by 400 and 100 it will be a leap year.This program accepts year as user input
   and verifies if the conditions for leap year is satisfied or not and print message to inform the user the same.
"""
def main():
    year=eval(input("Enter a year"))
    if year%400==0 :                         #This could be combined using or statement
        print("This is a leap year")
    elif year%100!=0 and year%4==0:
        print("This is a leap year")
    else:
        print("This is not a leap year")
main()
