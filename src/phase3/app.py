from flask import Flask, request, jsonify, render_template,redirect, url_for
import numpy as np
import joblib
import subprocess
import os
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
import webbrowser


app = Flask(__name__, template_folder='templates', static_folder='static')

# Load the trained model
model = joblib.load('linear_regression_model_2.pkl')

@app.route('/')
def index():
    return render_template('index.html', css_file='index.css')

@app.route('/prediction.html')
def prediction():
    return render_template('prediction.html', css_file='prediction.css')

@app.route('/cleaning_eda.html')
def clean_eda():
    return render_template('cleaning_eda.html')


@app.route('/predict', methods=['POST'])
def predict_price():
    # Get the input data from the request
    input_data = request.get_json()
    print(input_data)

    try:
        # Calculate YEAR_BUILT
        year_built = 2024 - int(input_data['AGE_OF_HOUSE'])
        input_data['YEAR_BUILT'] = year_built

        # Calculate TOTAL_HOUSE_AREA_sqft
        total_house_area = int(input_data['BASEMENT_sqft']) + int(input_data['ABOVE_BASEMENT_sqft'])
        input_data['TOTAL_HOUSE_AREA_sqft'] = total_house_area

        # Remove AGE_OF_HOUSE as it is no longer needed
        del input_data['AGE_OF_HOUSE']
        del input_data['CITY']
        
        print(input_data)
        
        attributes_order = ['NUM_OF_BEDROOMS','NUM_OF_BATHROOMS', 'LIVING_AREA_sqft', 'LOT_AREA_sqft', 'FLOORS', 'WATER_FRONT', 'ABOVE_BASEMENT_sqft', 'BASEMENT_sqft', 'VIEW_RATING', 'CONDITION_RATING', 'ZIP','YEAR_BUILT', 'TOTAL_HOUSE_AREA_sqft']

        # Create an array of values in the specified order
        input_values = [input_data[attr] if isinstance(input_data[attr], int) else int(input_data[attr]) for attr in attributes_order]
      
        print(input_values)

        # Convert input values to integers
        input_values = [int(value) for value in input_data.values()]
        print(input_values)

        # Reshape input values
        X = np.array([input_values]).reshape(1, -1)
        print(X)


        # Make a prediction using the model
        predicted_price = model.predict(X)[0]
        
        print(predicted_price)
        
        predicted_price = abs(predicted_price*0.0001)

        predicted_price = round(predicted_price, 2)

        # Return the predicted price as a JSON response
        return jsonify({'price': predicted_price})
    except (KeyError, ValueError):
        return jsonify({'error': 'Invalid data format'}), 400


@app.route('/clean_dataset', methods=['POST'])
def clean_dataset():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'success': False, 'message': 'No selected file'})
    
    if file:
        # Save the uploaded file
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        # Execute the clean_dataset.py script with the file path as argument
        subprocess.call(['python', 'clean_dataset.py', file_path])
        
        return jsonify({'success': True, 'message': 'Dataset cleaned successfully!'})
    else:
        return jsonify({'success': False, 'message': 'Error cleaning dataset'})


@app.route('/perform_eda', methods=['POST'])
def perform_eda():
    data = request.json
    eda_step = data.get('edaStep')
    print(f"Received EDA step: {eda_step}")
    if eda_step == 'Step 1':
        try:
            # Call the eda_step_1.py script
            subprocess.call(['python', 'eda_step_1.py'])
            image_path = 'static/eda_result1.png'  # Adjust the path accordingly
            return jsonify({'success': True, 'message': 'EDA Step 1 completed successfully!', 'image_path': image_path})
        except Exception as e:
            return jsonify({'success': False, 'message': f'Error performing EDA Step 1: {str(e)}'})
    elif eda_step == 'Step 2':
        try:
            # Call the eda_step_2.py script
            subprocess.call(['python', 'eda_step_2.py'])
            image_path = 'static/eda_result2.png'  # Adjust the path accordingly
            return jsonify({'success': True, 'message': 'EDA Step 2 completed successfully!', 'image_path': image_path})
        except Exception as e:
            return jsonify({'success': False, 'message': f'Error performing EDA Step 2: {str(e)}'})   
    elif eda_step == 'Step 3':
        try:
            # Call the eda_step_3.py script
            subprocess.call(['python', 'eda_step_3.py'])
            image_path = 'static/eda_result3.png'  # Adjust the path accordingly
            return jsonify({'success': True, 'message': 'EDA Step 3 completed successfully!', 'image_path': image_path})
        except Exception as e:
            return jsonify({'success': False, 'message': f'Error performing EDA Step 3: {str(e)}'})  
    elif eda_step == 'Step 4':
        try:
            # Call the eda_step_4.py script
            subprocess.call(['python', 'eda_step_4.py'])
            image_path = 'static/eda_result4.png'  # Adjust the path accordingly
            return jsonify({'success': True, 'message': 'EDA Step 4 completed successfully!', 'image_path': image_path})
        except Exception as e:
            return jsonify({'success': False, 'message': f'Error performing EDA Step 4: {str(e)}'})  
    elif eda_step == 'Step 5':
        try:
            # Call the eda_step_5.py script
            subprocess.call(['python', 'eda_step_5.py'])
            image_path = 'static/eda_result5.png'  # Adjust the path accordingly
            return jsonify({'success': True, 'message': 'EDA Step 5 completed successfully!', 'image_path': image_path})
        except Exception as e:
            return jsonify({'success': False, 'message': f'Error performing EDA Step 5: {str(e)}'}) 
    elif eda_step == 'Step 6':
        try:
            # Call the eda_step_6.py script
            subprocess.call(['python', 'eda_step_6.py'])
            image_path = 'static/eda_result6.png'  # Adjust the path accordingly
            return jsonify({'success': True, 'message': 'EDA Step 6 completed successfully!', 'image_path': image_path})
        except Exception as e:
            return jsonify({'success': False, 'message': f'Error performing EDA Step 6: {str(e)}'}) 
    elif eda_step == 'Step 7':
        try:
            # Call the eda_step_7.py script
            subprocess.call(['python', 'eda_step_7.py'])
            image_path = 'static/eda_result7.png'  # Adjust the path accordingly
            return jsonify({'success': True, 'message': 'EDA Step 7 completed successfully!', 'image_path': image_path})
        except Exception as e:
            return jsonify({'success': False, 'message': f'Error performing EDA Step 7: {str(e)}'}) 
    elif eda_step == 'Step 8':
        try:
            # Call the eda_step_8.py script
            subprocess.call(['python', 'eda_step_8.py'])
            image_path = 'static/eda_result8.png'  # Adjust the path accordingly
            return jsonify({'success': True, 'message': 'EDA Step 8 completed successfully!', 'image_path': image_path})
        except Exception as e:
            return jsonify({'success': False, 'message': f'Error performing EDA Step 8: {str(e)}'}) 
    elif eda_step == 'Step 9':
        try:
            # Call the eda_step_9.py script
            subprocess.call(['python', 'eda_step_9.py'])
            image_path = 'static/eda_result9.png'  # Adjust the path accordingly
            return jsonify({'success': True, 'message': 'EDA Step 9 completed successfully!', 'image_path': image_path})
        except Exception as e:
            return jsonify({'success': False, 'message': f'Error performing EDA Step 9: {str(e)}'}) 
    elif eda_step == 'Step 10':
        try:
            # Call the eda_step_10.py script
            subprocess.call(['python', 'eda_step_10.py'])
            image_path = 'static/eda_result10.png'  # Adjust the path accordingly
            return jsonify({'success': True, 'message': 'EDA Step 10 completed successfully!', 'image_path': image_path})
        except Exception as e:
            return jsonify({'success': False, 'message': f'Error performing EDA Step 10: {str(e)}'}) 
    else:
        return jsonify({'success': False, 'message': 'Invalid EDA step selected!'})

if __name__ == '__main__':
    app.run(debug=True)
