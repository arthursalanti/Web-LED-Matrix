from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <button onclick="fetch('/toggle')">Toggle</button>
    """

@app.route("/toggle")
def toggle():
    print("Hello World")  # prints in VS Code terminal
    return "OK"

app.run(debug=True)