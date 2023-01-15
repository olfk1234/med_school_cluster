from flask import Flask, render_template, request
import numpy as np
from joblib import load
import pandas as pd
app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def hello_world():
    request_type = request.method
    if request_type == "GET":
        return render_template("index.html")
    if request_type == "POST":
        mat_pct = request.form["Mat_pct"]
        mat_pct = float(mat_pct)
        avg_GPA = request.form["Avg_GPA"]
        avg_GPA = float(avg_GPA)
        mcat = request.form["MCAT"]
        mcat = float(mcat)
        state = request.form["state"]
        text_state = request.form["text_state"]
        test_np_input  = np.array([[mat_pct, avg_GPA, mcat]])
        model = load("kmean_sort.pkl")
        pca = load("pca_sort.pkl")
        scaler = load("scaler_sort.pkl")
        X_sc = scaler.transform(test_np_input)
        pca_X = pca.transform(X_sc)
        label = model.predict(pca_X)
        df = pd.read_csv("all_data.csv")
        if state == "Yes" and text_state != "":
            df_label = df[(df["label"].isin(label)) & (df["State"] == text_state.upper())]
            return render_template('results.html',  tables=[df_label.to_html(classes = ["table-bordered", "table-striped", "table-hover"])], titles = df_label.columns.values)
        elif (state == "Yes" and text_state == "") or state  == "No":
            df_label = df[(df["label"].isin(label))]
            return render_template('results.html',  tables=[df_label.to_html(classes = ["table-bordered", "table-striped", "table-hover"])], titles = df_label.columns.values)
                
        
@app.route("/methodology")
def methodology():
    return render_template("methodology.html")