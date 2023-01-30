import pandas as pd
import snscrape.modules.twitter as sntwitter 

query = "(datascience) until:2023-01-15 since:2022-10-11"
tweets=[]
limit=1000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
  if len(tweets)==limit:
    break
  else:
    tweets.append([tweet.date , tweet.id ,tweet.url ,tweet.user.username ,tweet.user.location ,tweet.content ,tweet.source ,tweet.retweetCount,tweet.likeCount ,tweet.replyCount,tweet.lang])
  
df = pd.DataFrame(tweets,columns=["Date", "Tweetid","tweet url", "username", "location","content","source", "retweetcount",  "likecount ","replycount","language"])
df

