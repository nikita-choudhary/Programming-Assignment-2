#3.	Write a Python program to display calendar?
import calendar
y = int(input("Enter the year : "))
m= int(input("Enter the month of the year in number(1 to 12) :"))
print(calendar.month(y,m))       #calling month function from calender module.