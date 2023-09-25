from flask import Flask, render_template

# create website object
app = Flask("website")

@app.route("/")
def go_home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>/")
def weather(station,date):
    temperature = 23
    return {"station":station,
            "date":date,
            "temperature":temperature}


if __name__=="__main__":
    app.run(debug=True)
