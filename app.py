# import necessary libraries
from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
from sklearn import tree
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier, export_graphviz


# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    return render_template("index.html")

# home page
@app.route("/home")
def home():
    return render_template("home.html")

def getNiceArray(basicArray):
    i = 0
    niceArray = []
    for entry in basicArray:
        niceEntry = {"id": i, "text": entry}
        niceArray.append(niceEntry)
        i += 1
    return niceArray

@app.route("/learn_more", methods=["GET"])
def learn_more():

    Final_Model_Data = pd.read_csv("Resources/Final_Model_Data.csv")
    # print(Final_Model_Data)

    # age_dropdown = Final_Model_Data["Age"].unique()
    age_entries = Final_Model_Data["Age"].unique()
    age_dropdown = getNiceArray(age_entries)
    
    gender_entries = Final_Model_Data["Gender"].unique()
    gender_dropdown = getNiceArray(gender_entries)

    state_entries = Final_Model_Data["State"].unique()
    state_dropdown =  getNiceArray(state_entries)

    offence_entries = Final_Model_Data["Offence"].unique()
    offence_dropdown =  getNiceArray(offence_entries)
#["0-19 years", "20-34 years"]
#[{"id": 0, "text": "0-19 years"}]
    return render_template("learn_more.html", data = {"age":age_dropdown, "gender":gender_dropdown, "state":state_dropdown, "offence":offence_dropdown})

# allow the use of POST request with methods=["POST"]
@app.route("/api/predict", methods=["GET","POST"])
def predict():
    if request.method == "POST":  # if the request method is POST
        x_values = request.get_json()  # get the json data
        print(x_values)
        model = joblib.load("model.pkl")  # load the model
        input_age = x_values["age"]
        print("'" + input_age + "'")
        if input_age == "0":
            age_result = 1,0,0,0
        elif input_age == "1":
            age_result = 0,1,0,0
        elif input_age == "2":
            age_result = 0,0,1,0
        elif input_age == "3":
            age_result = 0,0,0,1
        print(age_result)

        input_gender = x_values["gender"]
        if input_gender == "0":
            gender_result = 1,0
        elif input_gender == "1":
            gender_result = 0,1

        input_state = x_values["state"]
        if input_state == "0":
            state_result = 1,0,0,0,0,0,0,0
        elif input_state == "1":
            state_result = 0,1,0,0,0,0,0,0
        elif input_state == "2":
            state_result = 0,0,1,0,0,0,0,0
        elif input_state == "3":
            state_result = 0,0,0,1,0,0,0,0
        elif input_state == "4":
            state_result = 0,0,0,0,1,0,0,0
        elif input_state == "5":
            state_result = 0,0,0,0,0,1,0,0
        elif input_state == "6":
            state_result = 0,0,0,0,0,0,1,0
        elif input_state == "7":
            state_result = 0,0,0,0,0,0,0,1

        input_offence = x_values["offence"]
        if input_offence == "0":
            offence_result = 1,0,0,0,0,0
        elif input_offence == "1":
            offence_result = 0,1,0,0,0,0
        elif input_offence == "2":
            offence_result = 0,0,1,0,0,0
        elif input_offence == "3":
            offence_result = 0,0,0,1,0,0
        elif input_offence == "4":
            offence_result = 0,0,0,0,1,0
        elif input_offence == "5":
            offence_result = 0,0,0,0,0,1
        
        # print(offence_result)

        result = [offence_result + state_result + age_result + gender_result]

        print(result)

        prediction = model.predict(result)
        print(prediction)

        # return the predicted result
        return jsonify({"prediction": str(prediction[0])})



@app.route("/visualisation")
def visuals():
    return render_template("visualisation.html")


if __name__ == "__main__":
    app.run(debug=True)