class Student:
    def getdata(self,stid,stnm):
        print("ID:",stid)
        print("Name:",stnm)

st=Student()
#st.getdata(101,'Sanket')

stid=input("Enter an ID:")
stnm=input("Enter a Name:")
st.getdata(stid,stnm)
        