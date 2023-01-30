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

a_dict=a.to_dict("records")
print(a_dict)


from pymongo import MongoClient

py=MongoClient("mongodb://Guvi:@ac-wadx12y-shard-00-00.fr2x1n6.mongodb.net:27017,ac-wadx12y-shard-00-01.fr2x1n6.mongodb.net:27017,ac-wadx12y-shard-00-02.fr2x1n6.mongodb.net:27017/?ssl=true&replicaSet=atlas-jltwa6-shard-0&authSource=admin&retryWrites=true&w=majority")
pytweet=py["twitterscrapping"]
pycollection=pytweet["tweets"]
pycollection.insert_many(a_dict)


#note:done this project in google colab
