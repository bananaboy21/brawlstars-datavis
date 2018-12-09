import json
import matplotlib.pyplot as plt
import requests
import sys

config = json.load(open('auth.json'))
token = config['token']

r = requests.get('https://brawlapi.cf/api/leaderboards/players/20', headers={'Authorization': token})
data = r.json()
brawlers = {}

for player in data['players']:
    tag = player['tag']
    print(tag)
    r = requests.get('https://brawlapi.cf/api/players/{}'.format(tag), headers={'Authorization': token})
    playerdata = r.json()
    if 'brawlers' not in playerdata:
        print(playerdata)
        continue
    player_brawlers = playerdata['brawlers']
    def sortByTrophies(brawler):
        return brawler['trophies']
    player_brawlers.sort(key=sortByTrophies)
    top_brawler = player_brawlers[0]['name'].lower()
    if top_brawler in brawlers:
        brawlers[top_brawler] += 1
    else:
        brawlers[top_brawler] = 1

labels = list(set(brawlers.keys()))
sizes = [brawlers[x] * 10 for x in brawlers.keys()]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')

plt.savefig('brawler-dist.png')