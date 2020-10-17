import praw
import requests

r = praw.Reddit(
    client_id = "",
    client_secret = "",
    user_agent = "USERAGENT"
)

webhookURL = "https://discord.com/api/webhooks/762642495745687572/GDCocXRdIhzNpH4jhnDQQ8882ATHhYOnQmsA_tE4PCbV3N5gRMl-fqy-3An26iN4Z7z1"
memes = r.subreddit("memes+dankmemes")
for submission in memes.top('day'):
    requests.post(webhookURL, data = {'content': submission.url})
