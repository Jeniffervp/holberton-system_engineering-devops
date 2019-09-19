#!/usr/bin/python3
""" make a query to get the ten hot post in reddit """
from requests import get


def top_ten(subreddit):

    headers = {
        'User-Agent': 'Jeniffer'
    }
    try:
        redd = get('https://www.reddit.com/r/{}.json?limit=10&sort=hot'
                   .format(subreddit), headers=headers,
                   allow_redirects=False).json().get('data').get('children')
        for sub in redd:
            print(sub.get('data').get('title'))

    except:
        print(None)
