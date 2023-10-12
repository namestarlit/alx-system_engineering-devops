#!/usr/bin/python3
"""Queries the Reddit API

Rreturns a list containing the titles of all hot articles for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Prints titles of the first 10 hot posts listed for given subreddit"""
    res = requests.get("https://reddit.com/r/{}.json?sort=hot&limit=10"
                       .format(subreddit), headers={"User-agent": "custom"})

    if (res.status_code == 200):
        for i in res.json().get("data").get("children"):
            print(i.get("data").get("title"))
    else:
        print("None")
