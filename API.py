import requests

#namelist = []
#namelist.append(input("Please enter Username:"))  #Stored in namelist[0]
#namelist.append(input('Please enter Password:'))  #Stored in namelist[1]

r = requests.get('https://api.github.com/user/followers', auth=('C-Nev', 'Paudidog123'))

print (r.status_code)
print (r.headers['content-type'])
data = r.json()
{k: data[0].get(k, None) for k in ('login')}
print(k)
