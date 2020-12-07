import tweepy
from textblob import TextBlob #text/tweet parse
import re # regular expression


ck="Jm6WDXZuiwlwUnT9mFbPdSpcg"
cs="Wp4Gbf74R6MZWjXvj0ifKrCobwWbchhn53Mv8L7VMLbIUi6Wnd"
at="919434545924935681-wFjVVTbs0pmyB2VwSoj4VwGb7tBYCyr"
ats ="RaPfxU0rSMjkS3MSI9N0ztXu4I2iLMecXg79OerNHw4Ly"

auth = tweepy.OAuthHandler(ck, cs)
# set access token and secret
auth.set_access_token(at, ats)

# create tweepy API object to fetch tweets
api = tweepy.API(auth)


print(api,' login success')


def getSentiment(tweet):
     
        analysis = TextBlob(tweet)
        #print(analysis)
        #print(analysis.sentiment.polarity)
        
        # set sentiment
        
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
        
        #return analysis.sentiment.polarity


def clean_data(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())


def get_tweet(name,c=10):

    res = api.search(q=name,count=c)
    print('---------------',name,'--------------------')
    data= [] 
    for r in res:
        try:
            #print(getSentiment(clean_data(r.text)))
            data.append(getSentiment(clean_data(r.text)))
        except:
            pass
    return data


###
leaders = ['Narendra Modi','Rahul Gandhi','Sonia Gandhi','Priyanka Chopra']
for l in leaders:
    o = get_tweet(l)
    #print(o)
    p = 0
    n = 0
    ne = 0
    for i in o:
        if i =='positive':
            p+=1
        elif i =='negative':
            n+=1
        else:
            ne+=1

    print((p/len(o))*100 ,' ',(n/len(o))*100,' ',(ne/len(o))*100)
    
    



            
            
            
            






    
    
    











    
    
