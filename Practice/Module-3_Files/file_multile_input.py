file=open('stdata.txt','a')

n=int(input("Enter number of students:"))

for i in range(n):
    id=input("Enter your ID:")
    name=input("Enter your Name:")
    city=input("Enter your City:")
    
    file.write(f"ID:{id}\nName:{name}\nCity:{city}\n")
    file.write("\n-----------------\n")