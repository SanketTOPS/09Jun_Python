import pandas

stdata={
    'id':[1,2,3,4,5],
    'name':['sanket','ashok','nirav','hitesh','mahesh'],
    'city':['rajkot','surat','baroda','navsari','ahmedabad']
}

#print(stdata)

"""pd=pandas.DataFrame(stdata)
print(pd)"""

pd=pandas.read_csv('demo.csv')
data=pandas.DataFrame(pd)
print(data.to_string())