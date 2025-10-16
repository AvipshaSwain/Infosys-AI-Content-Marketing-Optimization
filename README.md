🧠 Infosys AI Content Marketing Optimization

This project, developed under the Infosys Mentorship Program, is an end-to-end AI-driven Content Marketing Optimizer.
It leverages Gemini 2.5 Flashlight as the base LLM to analyze, generate, and predict high-performing marketing tweets.
The system combines Twitter data, sentiment analysis, and LLM-based generation to identify and create tweets with maximum engagement potential.

🚀 Project Overview
🎯 Objective

To build an intelligent system that:

Analyzes marketing tweets for sentiment and engagement.

Trains an AI model using top-performing tweets.

Generates new tweets based on user prompts.

Predicts which generated tweet will perform better, with explanations.

⚙️ Workflow Summary
Step 1️⃣ — Data Extraction

50 tweets are extracted from a specific Twitter username using the Twitter API.

Each tweet includes key engagement metrics:

like_count

retweet_count

reply_count

quote_count

impression_count

All extracted tweets are stored in extracted_tweets.json.

Step 2️⃣ — Sentiment and Engagement Analysis

Script Used: sentiment-analysis.py

Each tweet is analyzed using Gemini 2.5 Flashlight to determine:

sentiment_type (positive / neutral / negative)

sentiment_score (from -1.0 to +1.0)

engagement_score (based on metrics like likes, retweets, replies, impressions)

Additional details such as keywords, topic, and target_audience

The enriched output is stored in analyzed_tweets.json.

Step 3️⃣ — LLM Training and Tweet Generation

The analyzed_tweets.json data is provided to the Gemini 2.5 Flashlight model.

The model:

Selects the Top 5 Best-Performing Tweets based on sentiment and engagement scores.

Uses these as reference training data.

Takes three inputs:

System Prompt — defines AI behavior and tone.

User Prompt — topic or message provided by the user.

Top 5 reference tweets — high-performing examples from the dataset.

Generates optimized and high-engagement tweets aligned with the user’s intent.

Step 4️⃣ — A/B Testing and Prediction Phase

Two tweets are generated for each user prompt.

Another instance of Gemini 2.5 Flashlight is used for A/B testing.

It compares both tweets and predicts:

Which tweet will perform better (based on engagement potential).

A clear explanation of why that tweet is predicted to perform better.

Comparative analysis of tone, emotion, clarity, and keyword strength.

The output includes:

User Prompt

Generated Tweet 1

Generated Tweet 2

Predicted Better Tweet

Explanation of Prediction

Step 5️⃣ — User Interface (UI)

The project features a simple interactive UI where:

The user enters a custom prompt.

The AI generates two tweets.

🧩 Example Workflow
User Prompt Example:

“Generate a tweet about the importance of AI in education.”

Generated Tweets:
TWEET A- “AI is transforming classrooms — from personalized tutoring to smarter assessments. The future of learning is intelligent. #AI #EdTech”
TWEET B- “Education meets innovation. AI empowers teachers to create personalized experiences for every learner. #AIinEducation #FutureReady”

Output:
Predicted Better Tweet: Tweet A
Explanation:
Tweet A uses stronger emotional language and informative keywords like “personalized tutoring” 
and “future of learning,” which increase engagement likelihood. The structure is concise and impactful.


The AI predicts which one will perform better.

The system displays both tweets and the explanation interactively.

🧠 Technologies Used
Category	Tools / Libraries
Base LLM	Gemini 2.5 Flashlight
Language	Python
APIs	Twitter API v2
Libraries	json, requests, time, pandas, nltk 
Interface	Flask / Streamlit / HTML
Storage	JSON-based structured datasets
