import requests

#namelist = []
#namelist.append(input("Please enter Username:"))  #Stored in namelist[0]
#namelist.append(input('Please enter Password:'))  #Stored in namelist[1]
auth=('C-Nev', 'Paudidog123')
r = requests.get('https://api.github.com/user', auth=auth)

print (r.status_code)
print (r.headers['content-type'])
data = r.json()
#{k: data.get(k, None) for k in ('login')}
print(data)
print('\n')
g = requests.get('https://api.github.com/user/followers', auth=auth)
data2 = g.text
for k, v in enumerate(data2):
    if v=='l':
        print("test")
        while v != ',':
            print (v)
