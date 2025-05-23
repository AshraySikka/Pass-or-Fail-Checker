m=int(input("Enter marks in Maths: "))
p=int(input("Enter marks in Physics: "))
c=int(input("Enter marks in Chem: "))
if m>100 or p>100 or c>100:
    print("Marks not in range for 1 or more subjects")
elif m>=45 and p>=45 and c>=45:
    print("Pass")
else:
    print("Not Pass")
