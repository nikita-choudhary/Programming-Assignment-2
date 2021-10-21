#4.	Write a Python program to solve quadratic equation?
import cmath             #imported for complex no.
a=int(input("Enter 1st coefficient : "))     #a,b,c are the constants in the equation 2x2+4x+4=0
b=int(input("Enter 2nd coefficient : "))
c=int(input("Enter 3rd coefficient : "))
#finding discriminant
d= b**2-4*a*c
print(d)
#the two solutions are :
a1 = (-b-cmath.sqrt(d))/2*a
a2 = (-b+cmath.sqrt(d))/2*a
print("The two solution of the quadratic equation 2x2 + 4x + 4 is ",a1 , a2)
