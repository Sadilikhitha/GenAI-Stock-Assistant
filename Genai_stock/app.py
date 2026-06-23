from flask import Flask, render_template, request, jsonify
from AI_agent.agent import run_agent

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    query = data["message"]

    response = run_agent(query)

    return jsonify({
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)