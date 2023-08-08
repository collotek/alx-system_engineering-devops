#!/usr/bin/python3
"""Script returns the numbers of
subscribers of subreddit passed to it"""

import requests


def number_of_subscribers(subreddit):
    """Function returns the numbers of
    subscribers of subreddit passed to it"""

    apiUrl = "https://reddit.com/r/{}/about.json".format(subreddit)
    userAgent = "Mozilla/5.0"

    response = requests.get(apiUrl, headers={"user-agent": userAgent})
    if not response:
        return 0
    retValue = response.json().get('data').get('subscribers')
    if retValue:
        return retValue
    else:
        return 0
