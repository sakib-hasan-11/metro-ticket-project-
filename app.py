from flask import Flask, render_template, request
import metro_ticket  # replace with your main module name

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_ticket():
    # adjust function name based on your code
    try:
        result = metro_ticket.main()  # or another function you have
    except Exception as e:
        result = f"Error: {e}"
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
