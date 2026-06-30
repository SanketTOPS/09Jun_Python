def getdata(id,name,city):
    print("ID:",id)
    print("Name:",name)
    print("City:",city)

n=int(input("Enter number of students:"))
for i in range(n):
    stid=input("Enter your ID:")
    stnm=input("Enter your Name:")
    stct=input("Enter your City:")
    getdata(stid,stnm,stct)
    print("---------------")

