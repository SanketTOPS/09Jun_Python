stdata={'id':101,
        'name':'sanket',
        'city':'rajkot'}

#print(stdata)
#print(stdata['id'])
#print(stdata.get('city'))
"""print(stdata.keys())
print(stdata.values())
print(stdata.items())"""

# ----------------- #
print(stdata)
print(len(stdata))

"""if 'name' in stdata:
    print('Yes...')
else:
    print('Noo')"""
    
"""if 'sanket' in stdata.values():
    print('Yes...')
else:
    print('Noo')"""
    
"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

for i,j in stdata.items():
    print(i,j)