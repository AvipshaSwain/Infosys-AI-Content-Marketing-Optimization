from create_tweet import create_tweet
from flask import Flask, request, jsonify
from flask_cors import CORS   # ✅ import

flask_app = Flask(__name__)
CORS(flask_app)  # ✅ allow requests from frontend

@flask_app.route("/")  # root or index route
def index():
    return "Hello Flask! This is a sample Flask app!"

@flask_app.route("/add/<num1>/<num2>")
def add_numbers(num1, num2):
    sum_num = int(num1) + int(num2)
    return f"This method will add numbers {num1} and {num2} ==> {sum_num}"

@flask_app.route("/generate")
def generate_tweet():
    prompt = request.args.get('prompt')
    tweet_creation_data = create_tweet(prompt)

    return jsonify({
    "prompt": prompt,
    "tweet_a": tweet_creation_data['tweet_a'],
    "tweet_b": tweet_creation_data['tweet_b'],
    "tweet_a_vs_b": tweet_creation_data['tweet_a_vs_tweet_b'],
    "prediction": tweet_creation_data['prediction'],
    "explanation": tweet_creation_data['explanation']
})


if __name__ == "__main__":
    flask_app.run(debug=True)   