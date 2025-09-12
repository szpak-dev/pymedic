from flask import Flask, render_template, request, redirect
from mc_data import persist_patient


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/new_patient")
def new_patient():
    patient_form = request.form.to_dict()
    persist_patient(patient_form)
    return redirect("/")


@app.post("/new_doctor")
def new_doctor():
    form_data = request.form.to_dict()
    return render_template("index.html", form_data=form_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
