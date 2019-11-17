import tweepy

#common words should be taken out of the file
commonWords = ['the', 'in', 'on', 'a', 'an', 'to', 'from', 'for', 'that', 'it', 'as', 'at', 'is', 'are', 'am', 'can',
               'be', 'was', 'were', 'and', 'or', 'he', 'she', 'of', 'by', 'they', 'we','i', 'my', 'have', 'if', 'will',
               'where', 'when', 'what', 'which', 'who', 'how']
# garbage is usually is going to be at the end of the word.
garbage =['.',',','?','!']
# This function will get rid of the garbage from the filter
def filter(str, separators):
    j = 0 # increment to 4
    i = -1 # index of garbages if not -1
    while i==-1 and j<4:
        i = str.find(separators[j])
        j += 1
    #At this point, if i != -1, we need to get rid of the garbage
    if i != -1:
        str = str[0:i]
    return str


#authenticate and get the api going
consumer_key = "rHnu6TYbhzmWjcBD5L7wkOQvA"
consumer_secret = "oFGNC8iQOg1uWVcHpwLJV4cwk26tSH7ILUbz1i3I6rA0Wp4VBX"
access_token = "1194396187526221824-F3DNWJhSOoX8xULFQXLl4VZ20VjPPW"
access_token_secret = "9hOAWPiKP9vjzE8hVSERqKsvOerGmrrp9ZN38N9vnd20X"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#ask for user name to search for
nameToSearch = input("Enter a name to search on Twitter people search bar: ")
userList = api.search_users(nameToSearch,10)

#print user options to choose from
i = 1
for users in userList:
    print(str(i)+': '+users.name +'\n'+ users.description)
    print()
    i += 1

#specify the user from 1 to 10
index = int(input("Which one is the one that you meant to search (give index between 1-10)"))
index -= 1
user = userList[index]

#save top 20 posts from the specified user and print words from "full_text" attribute to a csv file
userPosts = api.user_timeline(user_id = user.id, count = 20, tweet_mode = 'extended')
outputFile = open("recentWordsForUser.csv", "w")
# foreach loop to point every words that are not common words
for tweets in userPosts:
    tweet_body = tweets.full_text
    bodyWords = tweet_body.split() # if the text is retweet, it only saves first 20ish words
    # process and write each word by getting rid of garbage and not writing to a file if it is common word
    for word in bodyWords:
        newWord = filter(word,garbage)
        if(newWord.isalnum()):
            newWord = newWord.lower()
        if newWord.isalnum() and newWord not in commonWords:
            outputFile.write(newWord)
            outputFile.write(',')
outputFile.write(' \n')


# Maybe do wordCloud?? IDK
