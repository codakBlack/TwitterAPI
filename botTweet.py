import tweepy
consumer_key = "rHnu6TYbhzmWjcBD5L7wkOQvA"
consumer_secret = "oFGNC8iQOg1uWVcHpwLJV4cwk26tSH7ILUbz1i3I6rA0Wp4VBX"
access_token = "1194396187526221824-F3DNWJhSOoX8xULFQXLl4VZ20VjPPW"
access_token_secret = "9hOAWPiKP9vjzE8hVSERqKsvOerGmrrp9ZN38N9vnd20X"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

keyword = input("Enter the keyword that you want to examine at this time: ")

keyword_tweets = api.search(keyword) #I think this will give you latest tweets on keyword
for tweets in keyword_tweets:
    print(str(tweets.author) +': '+ str(tweets.text))

print("Nima")
