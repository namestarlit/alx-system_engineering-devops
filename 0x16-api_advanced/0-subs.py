#!/usr/bin/python3
"""Query Reddit API to get the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Retrives number of subscribers from a sub-reddit"""
    res = requests.get(f'https://reddit.com/r/{subreddit}/about.json',
                       headers={"User-agent": "custom"})

    if (res.status_code == 200):
        return res.json().get('data').get('subscribers')
    return 0
