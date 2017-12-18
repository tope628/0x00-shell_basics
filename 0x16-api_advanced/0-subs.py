#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """fetches subscriber info from reddit API"""
    link = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    red = requests.get(link, headers={'User-Agent': 'tope628'}).json()
    try:
        subs = red.get('data').get('subscribers')
    except:
        return 0
    if red is None:
        return 0
    return subs
