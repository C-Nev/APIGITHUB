import requests
import json
import random
import matplotlib.pyplot as plt

class user:
    lgn = 'NULL'
    id = 'NULL'
    name = 'NULL'
    location = 'NULL'
    repos = 'NULL'
    userSince = 'NULL'
    followers = 'NULL'
    following = 'NULL'
    followers_url = 'NULL'
    following_url = 'NULL'
    trackedUser = 'NULL'
    printStat = 'NULL'

    def __init__(self, userJSON, tracked):
        self.lgn = userJSON['login']
        self.id = userJSON['id']
        self.name = userJSON['name']
        self.location = userJSON['location']
        self.repos = userJSON['public_repos']
        self.userSince = userJSON['created_at']
        self.followers = userJSON['followers']
        self.following = userJSON['following']
        self.followers_url = userJSON['followers_url']
        self.trackedUser = tracked
        self.following_url = userJSON['following_url']
        if self.name is None:
            self.name = self.lgn
        if self.location is None:
            self.location = "No location"
        self.printStat = self.createPrintStat()
        print(self.name)
        print(self.id)

    def createPrintStat(self):
        printStat =      str(self.lgn) + ' Login \n' + \
                               str(self.id) + ', ID Number\n' + \
                               self.name + ', Name\n' + \
                               self.location + ', Location\n'+ \
                               str(self.repos) + ', Repos\n'+ \
                               self.userSince + ', UserSince\n'+ \
                               self.followers_url + ', Followers url\n'+ \
                               self.following_url + ', Following url\n'+ \
                               str(self.followers) + ', Followers\n'+ \
                               str(self.following) + ', Following\n' + \
                               str(self.trackedUser) + ' Tracked User )'
        return printStat




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
r = requests.get('https://api.github.com/users/WhelanB', auth=auth)     #an account with followers and is following people
print(r.status_code)

userJSON = json.loads(r.text or r.content)

initialUser = user(userJSON, 1)
followers_pie_chart(initialUser.followers, initialUser.following)
print(r.text)
print(initialUser.printStat)



