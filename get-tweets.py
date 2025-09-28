import json
import tweepy
from run_prompt import execute_gemini


API_KEY = "kTFkyXnkkH5VyNSrSKrbkKVhG"
API_KEY_SECRET = "gZYynuXRnHmhORyW09tvYhxPAk80vclAvpOCMgpcjjQzIp7cST"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAO8k3wEAAAAAT4CbDPxQsIMI4Ug%2BOC%2BTPGQ%2BhAc%3DAn7BnF5ubXdUTZGOQUeaqHGw3RLLPssKSDGsTEpBSnrH2MENDS"
ACCESS_TOKEN = "1960432475596808192-3IP4fCSnvwHAfW8pl6tGthJo2O79xT"
ACCESS_TOKEN_SECRET = "lo9YhgzpGFFf8jjBdc7ScAYNFw8a6xGeJRbd3yFtv8rR3"

if __name__ == "__main__":
    twitterClient = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=API_KEY_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
        wait_on_rate_limit=True,
    )

    # Get user info
    user = twitterClient.get_user(username="sundarpichai")  # type: ignore
    user_id = user.data.id

    # Get latest 5 tweets
    tweets = twitterClient.get_users_tweets(
        user_id,
        max_results=50,
        tweet_fields=['created_at', 'public_metrics', 'text']
    )

with open("extracted_tweets.json", "w") as json_file: 
    json.dump([tweet.data for tweet in tweets.data], json_file, indent=4)
