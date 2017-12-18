#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """fetches top ten info from reddit API"""
    link = 'http://www.reddit.com/r/{}/top.json'.format(subreddit)
    red = requests.get(link, headers={'User-Agent': 'tope628'}).json()
    try:
        subs = red.get('data').get('children')
        for x in range(0, 10):
            print(subs[x]['data'].get('title'))
    except:
        print(None)
