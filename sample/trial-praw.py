# -*- coding: utf-8 -*-
import os
import configparser

import praw
from dotenv import load_dotenv
from requests import Session

if __name__ == "__main__":
    # set env. args
    load_dotenv("../.env")
    # laod reddit config
    reddit_ini = configparser.ConfigParser()
    reddit_ini.read(
        "../reddit.ini",
        encoding="utf-8"
    )
    section = "MONITORING"
    client_id = reddit_ini.get(section, "client_id")
    client_secret = reddit_ini.get(section, "client_secret")
    user_agent = reddit_ini.get(section, "user_agent")
    username = reddit_ini.get(section, "username")
    password = reddit_ini.get(section, "password")

    session = Session()
    session.proxies['https'] = os.getenv("http_proxy")
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        username=username,
        password=password,
        requestor_kwargs={'session': session}
    )

    subreddit = reddit.subreddit('wallstreetbets')
    hot_posts = subreddit.hot(limit=100)

    for post in hot_posts:
        print(post.title)