
import requests
import json
import random
import matplotlib.pyplot as plt

def followers_pie_chart(int, int2):
    labels = 'Followers', 'Following'
    sizes = [int, int2]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()
    return

auth = ('C-Nev', '555abb9471e86d7488b68576993c79f902ca1855')
r = requests.get('https://api.github.com/users/WhelanB', auth=auth).json()     #an account with followers and is following people

print(r)
followers=r['followers']
following=r['following']
followingURL=r['following_url']
followers_pie_chart(followers, following)
print(followingURL)




