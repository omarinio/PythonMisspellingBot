import tweepy
from keys import *
import datetime

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main():
    search = 'adress OR arguement OR beggining OR definately'

    for tweet in tweepy.Cursor(api.search, search).items(10):
        currtime = str(datetime.datetime.now())
        try:
            tweetId = tweet.id_str
            username = tweet.user.screen_name
            if 'adress' in tweet.text:
                api.update_status("@" + username + " " + "Did you mean address?" + currtime,
                                in_reply_to_status_id=tweetId)
                print("replied correcting address")
            elif 'arguement' in tweet.text:
                api.update_status("@" + username + " " + "Did you mean argument?" + currtime,
                                  in_reply_to_status_id=tweetId)
                print("replied correcting argument")
            elif 'beggining' in tweet.text:
                api.update_status("@" + username + " " + "Did you mean beginning?" + currtime,
                                  in_reply_to_status_id=tweetId)
                print("replied correcting beginning")
            elif 'definately' in tweet.text:
                api.update_status("@" + username + " " + "Did you mean definitely?" + currtime,
                                  in_reply_to_status_id=tweetId)
                print("replied correcting definitely")


        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break


main()
