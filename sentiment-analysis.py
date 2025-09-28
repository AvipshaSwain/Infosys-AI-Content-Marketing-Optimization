import json
import time
from run_prompt import execute_gemini

with open("extracted_tweets.json") as extracted_tweets_file:
    extracted_tweets = json.load(extracted_tweets_file)

    analyzed_tweets = []

    for tweet in extracted_tweets:
        time.sleep(5)  # avoid quota/rate limits

        sentiment_analysis_prompt = f"""
        Tweet: {tweet["text"]}
        like_count: {tweet["public_metrics"]["like_count"]}
        retweet_count: {tweet["public_metrics"]["retweet_count"]}
        reply_count: {tweet["public_metrics"]["reply_count"]}
        impression_count: {tweet["public_metrics"]["impression_count"]}
        
        Analyze this tweet considering both text and engagement metrics.
        Provide: sentiment_type, sentiment_score (-1 to +1), keywords.
        """

        out_dict = execute_gemini(sentiment_analysis_prompt)  # already returns dict

        # Add tweet text for reference
        out_dict["tweet"] = tweet["text"]

        # Add engagement info too (optional)
        out_dict.update(tweet["public_metrics"])

        print(out_dict)
        analyzed_tweets.append(out_dict)

    # Save JSON file
    with open("analyzed_tweets.json", "w") as analyzed_tweets_file:
        json.dump(analyzed_tweets, analyzed_tweets_file, indent=2)
