from flask import Flask, request, jsonify

app = Flask(__name__)

# Health check
@app.route("/")
def home():
    return "Bot is running"

# Webhook endpoint (TradingView sends alerts here)
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    print("📩 Incoming Alert:", data)

    # Basic parsing (you can expand later)
    signal = data.get("signal", "NONE")

    if signal == "BUY":
        print("🟢 BUY SIGNAL RECEIVED")
    elif signal == "SELL":
        print("🔴 SELL SIGNAL RECEIVED")

    return jsonify({"status": "received"})
