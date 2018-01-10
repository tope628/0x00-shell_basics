#!/usr/bin/python3
import requests
from pprint import pprint


def recurse(subreddit, hot_list=[], after=None):
    link = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(link, headers={'User-Agent': 'tope628'},
                     params={'limit': 100, 'after': after})
    if r.status_code == 200:
        red = r.json()
        titles = red.get('data').get('children')
        for title in titles:
            hot_list.append(title.get('data').get('title'))
        after = red.get('data').get('after')
        if not after:
            return(hot_list)
        return(recurse(subreddit, hot_list, after))
    else:
        return None
