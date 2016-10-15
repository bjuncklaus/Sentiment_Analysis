import tweepy
from textblob import TextBlob
from mstranslator import Translator

"""
Libs:
    https://textblob.readthedocs.io/en/dev/
    https://pypi.python.org/pypi/mstranslator
"""
# Twitter info
consumer_key = 'GW8wstK6iPAn4UY4FgnxfTd2h'
consumer_secret = '6pIpAy32sOAATULfZqQWrXbe5sbXaQdUofPys1mSVlEMkIzKAa'

access_token = '104984260-whCiE24vIwPgnx8Ym41LxEy8dldRRNFu8fLbiGzs'
access_token_secret = 'oanaiTCnCPCnh1rHkMT7FxHAUeuT5NEnQZTGGnrITYmTd'

# Microsoft DataMarket for translation - limited plan for 2 million characters per month
client_id = 'bruno_sentiment_analysis'
client_secret = 'Kd/gHVZgXTkXoAEGaK/or71IrEQr1DmG98q8eLQmaGU='

# MS Translator
translator = Translator(client_id, client_secret)

# Language properties for translation
LANG_FROM = 'pt'
LANG_TO = 'en'

# Authenticating on twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# API fully authenticated
api = tweepy.API(auth)

# Tweets
SEARCH_TERM = 'unisul'
public_tweets = api.search(SEARCH_TERM)

"""
The polarity score is a float within the range [-1.0, 1.0].
The subjectivity is a float within the range [0.0, 1.0]where 0.0 is very objective and 1.0 is very subjective.
"""
for i in range(10):
    # Translated text
    text = translator.translate(public_tweets[i].text, lang_from=LANG_FROM, lang_to=LANG_TO)

    # Sentiment analysis
    analysis = TextBlob(text)

    print(text)
    print(analysis.sentiment)
