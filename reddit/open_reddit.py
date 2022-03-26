import praw
import config


def open_reddit(sub, num):
    '''
    Using information in config to retrive information from subreddit. (Works like API)
    '''
    reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent=config.user_agent)
    submissions = reddit.subreddit(sub).top('week', limit=num)
    top50 = [(submission.title, submission.selftext) for submission in submissions]
    return top50


def main():
    open_reddit('mamamoo', 50)

if __name__ == '__main__':
    main()