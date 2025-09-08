from flask import Flask, render_template, request


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/")
def new_patient():
    form_data = request.form.to_dict()
    return render_template("index.html", form_data=form_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
