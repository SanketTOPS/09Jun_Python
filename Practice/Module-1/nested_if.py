s1=int(input("Enter Subject'1 Mark:"))
s2=int(input("Enter Subject'2 Mark:"))
s3=int(input("Enter Subject'3 Mark:"))
s4=int(input("Enter Subject'4 Mark:"))

total=s1+s2+s3+s4
pr=total/4

print("Total:",total)
print("PR:",pr)

if s1>=40 and s2>=40 and s3>=40 and s4>=40: #parent-root

    if pr>=70: #child
        print("Result:A")
    elif pr>=60: #child
        print("Result:B")
    elif pr>=50: #child
        print("Result:C")
    elif pr>=40: #child
        print("Result:D")
else:
    print("Result:FAIL")