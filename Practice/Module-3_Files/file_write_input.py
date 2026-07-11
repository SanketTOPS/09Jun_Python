file=open("hello.txt","a")

id=input("Enter an ID:")
name=input("Enter your Name:")
city=input("Enter your City:")

file.write(f"ID:{id}")
file.write(f"\nName:{name}")
file.write(f"\nCity:{city}")
