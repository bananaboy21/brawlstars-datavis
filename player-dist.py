# player-dist generates a pie chart of the distribution of clubs in the top players

import json
import sys
import requests
import matplotlib.pyplot as plt

config = json.load(open('auth.json'))
token = config['token']
playersize = sys.argv[1] if len(sys.argv) > 1 else 20

r = requests.get('https://brawlapi.cf/api/leaderboards/players/{}'.format(playersize), headers={'Authorization': token})
data = r.json()
clubs = {}
for player in data['players']:
    if player['clubName'] in clubs:
        clubs[player['clubName']] += 1
    else:
        clubs[player['clubName']] = 1

labels = list(set([x['clubName'] for x in data['players']]))
sizes = [clubs[x] * 100 for x in clubs.keys()]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')

plt.savefig('pie{}.png'.format(playersize))
