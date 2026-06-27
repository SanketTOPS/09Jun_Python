stdata={'id':[1,2,3,4,5],
        'name':['sanket','nirav','darshan','gopal','hitesh'],
        'sub':['c','c++','ds','html','css']
        }

#print(stdata)
#print(stdata["id"])
#print(stdata["id"][0])

for i,j in stdata.items():
    print(i,j[0])