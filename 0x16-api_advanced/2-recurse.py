#!/usr/bin/python3
""" make a query to get the ten hot post in reddit """
from requests import get


def recurse(subreddit, hot_list=[], after='null'):
    """  """
    headers = {
        'User-Agent': 'Jeniffer'
    }
    try:
        redd = 'https://www.reddit.com/r/{}.json'.format(subreddit)
        if after:
            redd = redd + '?after={}'.format(after)
        subs = get(redd, headers=headers,
                   allow_redirects=False).json().get('data').get('children')
        for tt in subs:
            hot_list.append(tt.get('data').get('title'))
        after = get(redd, headers=headers,
                    allow_redirects=False).json().get('data').get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except:
        return None
