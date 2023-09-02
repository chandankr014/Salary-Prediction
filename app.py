from flask import Flask, request, render_template, url_for
import joblib
import json

app = Flask(__name__)

# Load your machine learning model
model = joblib.load('random_forest_regressor.pkl')


# function
file_name = "job_company_dict.json"
with open(file_name, 'r') as file:
    data = json.load(file)

def get_label(job_company):
    label = data[job_company]
    return label


# define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input from HTML form
        minSlr = float(request.form.get("feature1"))
        maxSlr = float(request.form.get("feature2"))
        AvgExp = float(request.form.get("feature3"))
        job = str(request.form.get("feature4"))
        company = str(request.form.get("feature5"))
        job_company = job+"_"+company
        job_company_label = get_label(job_company)
        input_data = [minSlr, maxSlr, AvgExp, job_company_label]

        # Make a prediction using the model
        prediction = model.predict([input_data])[0]
        pred = int(prediction)

        return render_template('index.html', prediction="Predicted Salary is: "+str(pred))
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
