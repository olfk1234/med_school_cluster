from flask import Flask, render_template, request
import numpy as np
from joblib import load
import pandas as pd
import tkinter
from tkinter import messagebox
app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def hello_world():
    root = tkinter.Tk()
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
        if mat_pct > 100 or mat_pct <0:
            root.withdraw()
            root.lift()
            root.attributes('-topmost',True)
            messagebox.showwarning("Matriculation Percentage Out of Range", "Please input a percentage between 0 and 100")
            root.mainloop()
            return render_template("index.html")
        elif avg_GPA > 4 or avg_GPA <0:
            root.withdraw()
            root.lift()
            root.attributes('-topmost',True)
            messagebox.showwarning("GPA Out of Range", "Please input a GPA between 0 and 4")
            root.mainloop()
            return render_template("index.html")
        elif mcat > 528 or mcat < 472:
            root.withdraw()
            root.lift()
            root.attributes('-topmost',True)
            messagebox.showwarning("MCAT Out of Range", "Please input a MCAT between 472 and 528")
            root.mainloop()
            return render_template("index.html")
        else:
            test_np_input  = np.array([[mat_pct, avg_GPA, mcat]])
            model = load("kmean_sort.pkl")
            pca = load("pca_sort.pkl")
            scaler = load("scaler_sort.pkl")
            X_sc = scaler.transform(test_np_input)
            pca_X = pca.transform(X_sc)
            label = model.predict(pca_X)
            df = pd.read_csv("all_data.csv")
            if state == "Yes" and text_state != "":
                df_label = df[(df["label"].isin(label)) & (df["State"] == text_state)]
                return render_template('results.html',  tables=[df_label.to_html(classes = ["table-bordered", "table-striped", "table-hover"])], titles = df_label.columns.values)
            elif state == "Yes" and text_state == "":
                root.withdraw()
                root.lift()
                root.attributes('-topmost',True)
                messagebox.showwarning("Enter State", "Either enter a state or check 'No' for the 'Show only one state?' question")
                root.mainloop()
                return render_template("index.html")
            elif state  == "No":
                df_label = df[(df["label"].isin(label))]
                return render_template('results.html',  tables=[df_label.to_html(classes = ["table-bordered", "table-striped", "table-hover"])], titles = df_label.columns.values)
        root.mainloop()
        
@app.route("/methodology")
def methodology():
    return render_template("methodology.html")