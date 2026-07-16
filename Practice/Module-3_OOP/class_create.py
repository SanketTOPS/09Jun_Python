class Student:
    stid=12
    stnm="Sanket"
    
    def getdata(self):
        print("This is Student class!")
    
    def getsum(self,a,b):
        print("Sum:",a+b)

st=Student() #object of class
print("ID:",st.stid)
print("Name:",st.stnm)
st.getdata()
st.getsum(23,65)

    