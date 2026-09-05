from flask import Flask, render_template, request
import LinearRegressionGrades

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"

@app.route("/page1/")
def page():
    return render_template("home.html")

@app.route("/LinearRegression/", methods=["GET", "POST"])
def LRegressionGrades():
    calculateGradeResult = None
    if request.method == "POST":
        hours = float(request.form["hours"])
        calculateGradeResult = LinearRegressionGrades.calculateGrade(hours)
    return render_template ("templateLinearRegression.html", result= calculateGradeResult)  