from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    form_data = {
        'crop_yield': '',
        'co2_levels': '',
        'precipitation': '',
        'temperature': '',
        'soil_health': '',
        'fertilizer_use': '',
        'pesticide_levels': '',
        'irrigation_quality': '',
        'farming_practices': ''
    }

    if request.method == 'POST':
        # Collect form data
        form_data['crop_yield'] = request.form.get('crop_yield')
        form_data['co2_levels'] = request.form.get('co2_levels')
        form_data['precipitation'] = request.form.get('precipitation')
        form_data['temperature'] = request.form.get('temperature')
        form_data['soil_health'] = request.form.get('soil_health')
        form_data['fertilizer_use'] = request.form.get('fertilizer_use')
        form_data['pesticide_levels'] = request.form.get('pesticide_levels')
        form_data['irrigation_quality'] = request.form.get('irrigation_quality')
        form_data['farming_practices'] = request.form.get('farming_practices')
        
        # Example prediction logic
        prediction = f"Prediction Result: {float(form_data['crop_yield']) * 2}"  # Replace with your model

    return render_template('index.html', prediction=prediction, form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
