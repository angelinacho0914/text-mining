import praw
import config
reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent=config.user_agent)
sub = 'Genshin_Impact'
submissions = reddit.subreddit(sub).top('day', limit=5)
top5 = [(submission.title, submission.selftext) for submission in submissions]

print(submissions)
print(top5)