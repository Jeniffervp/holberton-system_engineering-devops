#!/usr/bin/python3
""" make a query to get the number of subscribers in reddit """
from requests import get


def number_of_subscribers(subreddit):

    headers = {
        'User-Agent': 'Jeniffer'
    }
    try:
        redd = get('https://www.reddit.com/r/{}/about.json'
                   .format(subreddit), headers=headers,
                   allow_redirects=False).json()
        subs = redd.get('data').get('subscribers')
        return subs

    except:
        return 0
