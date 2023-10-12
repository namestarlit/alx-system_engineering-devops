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
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    if next_page:
        url += '?after={}'.format(next_page)
    headers = {'User-Agent': 'custom'}

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return None

    data = res.json()['data']
    posts = data['children']
    for post in posts:
        count = count + 1
        hot_list.append(post['data']['title'])

    next_page = data['after']
    if next_page is not None:
        return recurse(subreddit, hot_list, next_page, count)
    else:
        return hot_list
