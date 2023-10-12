#!/usr/bin/python3
""" queries the Reddit API

Returns a list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Sends a recurse request to Reddit API

    Returns:
        List: containing titles of all hot articles for given subreddit
        None: if no results found
    """
    res = requests.get("https://reddit.com/r/{}/hot.json?after={}"
                       .format(subreddit, after),
                       headers={"User-agent": "custom"})

    if res.status_code != 200:
        return None
    if after is None:
        return hot_list

    for i in res.json().get("data").get("children"):
        hot_list.append(i.get("data").get("title"))
    after = res.json().get("data").get("after")

    return recurse(subreddit, hot_list, after)
