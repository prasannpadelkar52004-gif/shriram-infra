from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/services/details")
def services_details():
    return render_template("services_details.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# REMOVE debug=True
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
