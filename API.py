
import requests
import json
import random
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

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

    plt.bar(y_pos, performance, align='center',label='Followbacks', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('%')
    plt.xlabel(str(r['login']))
    plt.title('Ratio of followbacks')

    plt.show()
    return

def repos(response):

    reposList = []
    reposURL = r['repos_url']
    followingURL = r['following_url']
    if followingURL.endswith('{/other_user}'):
        followingURL = followingURL[:-13]



    t = requests.get(reposURL, auth=auth).json()
    t = requests.get(followingURL, auth=auth).json()

    y = 0
    followingList = []
    followingLista = []
    while y < len(t):
        name = t[y]['repos_url']
        followingList.append(name + ', ')
        y += 1

    for x in range(0, len(followingList)):
        if followingList[x].endswith(', '):
            followingList[x] = followingList[x][:-2]

    d=0
    while d<len(followingList):
        p = requests.get(followingList[d], auth=auth).json()
        j = t[d]['login']
        followingLista.append(len(p))
        reposList.append(str(j) + ', ')

        d+=1
    followingTuple = zip(followingLista, reposList)
    followingTuple = sorted(followingTuple)
    followingLista =([ a for a,b in followingTuple ], [ b for a,b in followingTuple ])
    n_groups = len(followingList)
    reposNum = followingLista[0]

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.35

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, reposNum, bar_width,
                     alpha=opacity,
                     color='b',
                     error_kw=error_config,
                     label='Repos')

    plt.xlabel('Login')
    plt.ylabel('Repos')
    plt.title('Number of repos in social circle of '+str(r['login']))
    plt.xticks(index + bar_width / 2, followingLista[1])
    plt.legend()

    plt.tight_layout()
    plt.show()
    return

def socialGraph(response):
    followingURL = r['following_url']
    followersURL = r['followers_url']
    if followingURL.endswith('{/other_user}'):
        followingURL = followingURL[:-13]
    if followersURL.endswith('{/other_user}'):
        followersURL = followersURL[:-13]

    t = requests.get(followingURL, auth=auth).json()
    s = requests.get(followersURL, auth=auth).json()
    y = 0
    followingList = []
    followersList = []
    color_list =[]
    while y < len(t):
        name = t[y]['login']
        followingList.append(name)
        y += 1
    y =0
    while y < len(s):
        namef = s[y]['login']
        followersList.append(namef)
        y += 1
    y=0
    G = nx.Graph()
    while y<len(followingList):
        G.add_edges_from(
           [(str(r['login']), followingList[y])])
        y += 1
        color_list.append('r')
    y=0
    while y < len(followersList):
          G.add_edges_from(
          [(str(r['login']), followersList[y])])
          color_list.append('g')
          y += 1


    nx.draw_networkx(G, with_labels=True, node_color=color_list)
    plt.show()
    return
auth = ('C-Nev', '555abb9471e86d7488b68576993c79f902ca1855')
r = requests.get('https://api.github.com/users/'+'WhelanB', auth=auth).json()     #an account with followers and is following people
percentageFollowback(r)
followers_pie_chart(r)
repos(r)
socialGraph(r)