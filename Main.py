from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    score = float(data.get("ai_score", 0))

    if score >= 65:
        decision = "TAKE TRADE"
    else:
        decision = "SKIP TRADE"

    print(f"{decision} | Score: {score}")

    return jsonify({"decision": decision})
