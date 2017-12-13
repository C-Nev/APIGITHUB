
import requests
import json
import random
import matplotlib.pyplot as plt
import numpy as np

def followers_pie_chart(response):
    followers = r['followers']
    following = r['following']
    labels = 'Followers', 'Following'
    sizes = [followers, following]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()
    return

def percentageFollowback(response):
    followingURL = r['following_url']
    followersURL = r['followers_url']
    if followingURL.endswith('{/other_user}'):
        followingURL = followingURL[:-13]
    if followersURL.endswith('{/other_user}'):
        followersURL = followersURL[:-13]


    t = requests.get(followingURL).json()
    y = 0
    followingList = []
    followersList = []
    while y < len(t):
        name = t[y]['login']
        followingList.append(name + ', ')
        y += 1
    q = requests.get(followersURL).json()
    y = 0
    while y < len(q):
        name = q[y]['login']
        followersList.append(name + ', ')
        y += 1
    biggestList = 0
    if followingList > followersList:
        biggestList = len(followingList)
    else:
        biggestList = len(followersList)
    matchingFollowersSet = set(followersList) & set(followingList)
    percentageFollowbacks = (len(matchingFollowersSet) / biggestList) * 100
    objects = ''
    y_pos = np.arange(1)
    performance = [100, percentageFollowbacks]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('%')
    plt.title('Ratio of followbacks')

    plt.show()
    return

def repos(response):
    y = 0
    reposURL = r['repos_url']
    followingURL = r['following_url']
    followersURL = r['followers_url']
    if followingURL.endswith('{/other_user}'):
        followingURL = followingURL[:-13]
    if followersURL.endswith('{/other_user}'):
        followersURL = followersURL[:-13]



    t = requests.get(reposURL).json()
    print (len(t))
    t = requests.get(followingURL).json()
    print (t)
    y = 0
    followingList = []
    followersList = []
    while y < len(t):
        name = t[y]['repos_url']
        followingList.append(name + ', ')
        y += 1

    for x in range(0, len(followingList)):
        if followingList[x].endswith(', '):
            followingList[x] = followingList[x][:-2]

    d=0
    print(followingList)
    while d<len(followingList):

        t = requests.get(followingList[d]).json()
        print(len(t))
        d+=1
    return
auth = ('C-Nev', '555abb9471e86d7488b68576993c79f902ca1855')
r = requests.get('https://api.github.com/users/WhelanB', auth=auth).json()     #an account with followers and is following people
#percentageFollowback(r)
#followers_pie_chart(r)
repos(r)