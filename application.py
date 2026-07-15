from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
cors = CORS(app)
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car_data.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()

    companies.insert(0, 'Select Company')
    return render_template('index.html',
                           companies=companies,
                           car_models=car_models,
                           years=year,
                           fuel_types=fuel_type)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        company    = request.form.get('company')
        name       = request.form.get('car_models')
        year_value = request.form.get('year')
        fuel_type  = request.form.get('fuel_type')
        kms_value  = request.form.get('kilo_driven')

        if not all([company, name, year_value, fuel_type, kms_value]):
            return "Missing fields", 400

        year       = int(year_value)
        kms_driven = int(kms_value)

        input_df = pd.DataFrame(
            [[company, name, year, kms_driven, fuel_type]],
            columns=['company', 'name', 'year', 'kms_driven', 'fuel_type']
        )

        prediction = model.predict(input_df)

        # Always return a plain number - frontend handles formatting
        return str(round(float(prediction[0]), 2))

    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    app.run(debug=True)
