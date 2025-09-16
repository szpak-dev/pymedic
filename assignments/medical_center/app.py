from flask import Flask, render_template, request, redirect
from mc_data import validate_form, is_bool, _bool_map
from mc_generate_id import generate_id

app = Flask(__name__)



@app.get("/")
def index():
    return render_template("index.html")


@app.post("/")
def new_patient():
    form_data = request.form.to_dict()
    form_data['id'] = generate_id()

    form_errors = validate_form(form_data)

    if not form_errors:
        pass

    return render_template("index.html", form_data=form_data, form_errors = form_errors)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
