import praw

##
## Super simple python script to print out the text of the most
## recent comments from a given user (currently set to 25 most
## recent from qkme_transcriber). Just run python get_comments.py
## and enter your reddit username when prompted.
##
## Don't forget to install praw (https://github.com/praw-dev/praw)
##

# Begin connection to reddit
reddit_name = raw_input('What is your reddit username? ').strip()
user_agent = ('Meme text grabber by /u/{}'.format(reddit_name))
r = praw.Reddit(user_agent=user_agent)

# Connect to user in question
user_name = "qkme_transcriber"
user = r.get_redditor(user_name)

# Get their comments
num_comments = 25
generator = user.get_comments(25)

# Get information about the comments
for comment in generator:
    print comment.body + '/n'
    print comment.submission
    print '---------------------------------'

